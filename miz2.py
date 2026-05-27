"""
miz2.py: Receives data from miz.py, processes it, and passes to miz3.py.
"""

from typing import dict
from miz3 import write_to_output
from datetime import datetime


def process_stage2(data: dict) -> dict:

    print(f"[miz2.py] Received data from stage 1")
    
    # Stage 2 processing: Add metadata and transformations
    enriched_data = {
        **data,
        "word_count": len(data.get("processed_text", "").split()),
        "character_count": len(data.get("processed_text", "")),
        "reversed_text": data.get("processed_text", "")[::-1],
        "stage": 2,
        "stage2_timestamp": datetime.now().isoformat()
    }
    
    print(f"[miz2.py] Stage 2 enrichment completed")
    print(f"[miz2.py] Word count: {enriched_data['word_count']}")
    
    result = write_to_output(enriched_data)
    
    return result
