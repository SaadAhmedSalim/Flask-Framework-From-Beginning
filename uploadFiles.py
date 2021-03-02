from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('uploadFiles.html')

@app.route('/uploader', methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'File Uploaded Successfully!'

if __name__ == '__main__':
    app.run(debug=True)