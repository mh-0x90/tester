import sys
from users import check_user
from logger import log_activity
from auditor import audit
from health import check_health
from version import show_version

check_health()
show_version()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <username> <input> [--log]")
        sys.exit(1)

    try:
        username = sys.argv[1]
    except Exception as e:
        print(f"Invalid username: {e}")
        sys.exit(1)

    user_input = sys.argv[2]
    mode = sys.argv[3] if len(sys.argv) > 3 else ""

    if mode == "--log":
        log_activity(username)
    elif mode == "--audit":
        audit(username)
    else:
        check_user(username, user_input)
