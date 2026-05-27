"""
miz.py: Exposes a GET API endpoint and passes data through the pipeline.
"""

from flask import Flask, request, jsonify
from miz2 import process_stage2
from datetime import datetime
import transformer
app = Flask(__name__)


def processing_stage1(data: str) -> dict:

    data = transformer.pashmak(data)

    processed = {
        "original_input": data,
        "processed_text": data.upper(),
        "input_length": len(data),
        "timestamp": datetime.now().isoformat(),
        "stage": 1
    }
    return processed


@app.route("/whatever", methods=["GET"])
def handle_get_request():

    input_data = request.args.get("data", "")
    
    if not input_data:
        return jsonify({
            "status": "error",
            "message": "Missing 'data' query parameter"
        }), 400
    
    
    stage1_result = processing_stage1(input_data)
    print(f"[miz.py] Stage 1 processing completed")
    
    stage2_result = process_stage2(stage1_result)
    print(f"[miz.py] Stage 2 processing completed")
    
    return jsonify({
        "status": "success",
        "message": "Data processed through complete pipeline",
        "result": stage2_result
    })




if __name__ == "__main__":
    app.run(debug=True, port=5001)
