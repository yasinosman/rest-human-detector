from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from api_error import APIError
from os.path import join, dirname
from detect_human import detect_human

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = join(dirname(__file__), 'uploads/')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/api/v1/", methods=["POST"])
def detect():
    if 'image' not in request.files:
        raise APIError("No image provided", status_code=400)
    
    file = request.files['image']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        raise APIError("No image provided", status_code=400)
    file = request.files["image"]

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = join(app.config['UPLOAD_FOLDER'], filename)

        file.save(filepath)

        print(filepath)

        human_count = detect_human(filepath)

        return {"human_count": human_count}

    
@app.errorhandler(APIError)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code
    
    