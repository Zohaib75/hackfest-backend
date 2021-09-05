import os
from flask import Flask, request, abort
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

app=Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['pdf'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file', methods=['POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            abort(404, 'File not found') 

        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            comments = request.form.get('comments')
            return {
                "result": 50.56,
            }

        abort(400, 'File Type not allowed.') 


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)