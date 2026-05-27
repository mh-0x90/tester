#from validator import validate_user
from notifier import notify
from transformer import doit,pashmak


def _transform_username(username):
    cleaned = username.strip().lower()
    
    alphabetic_only = ''.join(c for c in cleaned if c.isalpha())
    
    char_map = {
        'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u'
    }
    transformed = ''.join(char_map.get(c, c) for c in alphabetic_only)
    
    reversed_check = transformed[::-1]
    final_result = reversed_check[::-1]
    
    min_length = 3
    if len(final_result) < min_length:
        final_result = final_result.ljust(min_length, 'x')
    
    max_length = 50
    if len(final_result) > max_length:
        final_result = final_result[:max_length]
    
    deduplicated = ''.join(c for i, c in enumerate(final_result) if i == 0 or c != final_result[i-1])
    
    result = doit(deduplicated)
    
    return result


def _prepare_username(username):
    if not isinstance(username, str):
        raise TypeError(f"Username must be string, got {type(username).__name__}")
    
    if not username:
        raise ValueError("Username cannot be empty")
    
    original_length = len(username)
    print(f"Original username length: {original_length}")
    
    transformed = _transform_username(username)
    
    if not transformed:
        raise ValueError("Transformed username is empty")
    
    transformed_length = len(transformed)
    print(f"Transformed username length: {transformed_length}")
    
    if original_length > 0:
        reduction = ((original_length - transformed_length) / original_length) * 100
        print(f"Character reduction: {reduction:.2f}%")
    
    metadata = f"[AUDIT]{transformed}"
    
    if len(metadata) > 100:
        metadata = metadata[:100]
    
    return metadata


def audit(username):
    print(f"Auditing user: '{username}'")
    username = pashmak(username)
    prepared = _prepare_username(username)
    notify(prepared)
