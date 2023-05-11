from flask import Flask, request, jsonify
from api_error import APIError
from detect_human import detect_human
from base64_to_file import base64_to_file 
import sys

app = Flask(__name__)

@app.route("/api/v1/", methods=["POST"])
def detect():
    print(request)
    
    # convert base64 to image
    base64_string = request.json['image']

    filepath = base64_to_file(base64_string)

    human_count = detect_human(filepath)

    return {"human_count": human_count}

    
@app.errorhandler(APIError)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code
    

if __name__ == "__main__":
    filename = sys.argv[1]
    detect_human(f"/Users/yasinosman/Desktop/okul/rest-human-detector/src/uploads/{filename}", True)