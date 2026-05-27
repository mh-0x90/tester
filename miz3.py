"""
miz3.py: Receives data from miz2.py and writes it to a text file.
"""

from typing import dict
from datetime import datetime


def write_to_output(data: dict, filename: str = "pipeline_output_miz.txt") -> dict:

    print(f"[miz3.py] Received data from stage 2")
    
    try:
        with open(filename, "w") as f:
            f.write("=" * 80 + "\n")
            f.write("PIPELINE OUTPUT REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            
            # Original Input
            f.write("ORIGINAL INPUT:\n")
            f.write("-" * 80 + "\n")
            f.write(f"{data.get('original_input', '')}\n\n")
            
            # Stage 1 Results
            f.write("STAGE 1 PROCESSING RESULTS:\n")
            f.write("-" * 80 + "\n")
            f.write(f"Input Length: {data.get('input_length', 0)} characters\n")
            f.write(f"Processed Text (Uppercase): {data.get('processed_text', '')}\n")
            f.write(f"Timestamp: {data.get('timestamp', '')}\n\n")
            
            # Stage 2 Results
            f.write("STAGE 2 PROCESSING RESULTS:\n")
            f.write("-" * 80 + "\n")
            f.write(f"Word Count: {data.get('word_count', 0)}\n")
            f.write(f"Character Count: {data.get('character_count', 0)}\n")
            f.write(f"Reversed Text: {data.get('reversed_text', '')}\n")
            f.write(f"Timestamp: {data.get('stage2_timestamp', '')}\n\n")
            
            # Complete Data
            f.write("COMPLETE DATA OBJECT:\n")
            f.write("-" * 80 + "\n")
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
            
            f.write("\n" + "=" * 80 + "\n")
            f.write("END OF REPORT\n")
            f.write("=" * 80 + "\n")
        
        print(f"[miz3.py] Successfully written to {filename}")
        
        return {
            "status": "success",
            "file": filename,
            "message": "Data successfully written to file",
            "stage": 3
        }
    
    except IOError as e:
        print(f"[miz3.py] Error writing to file: {e}")
        return {
            "status": "error",
            "message": str(e),
            "stage": 3
        }
