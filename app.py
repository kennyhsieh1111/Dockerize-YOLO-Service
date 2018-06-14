from flask import Flask, request, url_for, render_template, send_from_directory, redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug import secure_filename
import os, time

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/opt/Dockerize-YOLO-Service/darknet'

# Check the upload extension whether is images or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

## Directory : create the directory of upload image 
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

## Directory : create the directory of detected image
@app.route('/detect/<filename>')
def detect_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Dashboard
@app.route('/', methods=['GET', 'POST'])
def upload():
    # Redirect to Upload page
    upload_url=""
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            upload_url = url_for('uploaded_file', filename=filename)
        return redirect(url_for('uploaded', filename=filename))
    return render_template('index.html')

# Upload 
@app.route('/uploaded/<filename>', methods=['GET', 'POST'])
def uploaded(filename):
    upload_image = url_for('uploaded_file', filename=filename)

    # Redirect to Detected page
    if request.method == 'POST':
        # Trigger yolo detection
        # Tiny version : yolov3-tiny
        os.chdir(app.config['UPLOAD_FOLDER'])
        os.system('./darknet detect cfg/yolov3.cfg yolov3.weights ' + filename)
        os.system('mv predictions.png ' + filename + '-predict.png' )
        os.system('cp ' + filename + '-predict.png ../static/') # move to static dir
        os.system('rm ' + filename)
        os.system('rm ' + filename + '-predict.png')
        return redirect(url_for('detected', filename=filename))

    return render_template('upload.html', upload_image=upload_image)

# Detection
@app.route('/detected/<filename>', methods=['GET', 'POST'])
def detected(filename):
    upload_image = url_for('uploaded_file', filename=filename)
    detect_image = url_for('static', filename=filename + '-predict.png')
    
    # Redirect to Upload page
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            upload_url = url_for('uploaded_file', filename=filename)
        return redirect(url_for('uploaded', filename=filename))

    # Read the prediction label txt
    with open("prediction_label.txt", "r") as lab:
        label_class = []
        for line in lab:
            label_class = [line.rstrip() for line in lab]

    # Remove the dulplicate items, and calculate the numbers of classes
    label_class = set(label_class)
    lebel_len = len(label_class)
    label_class = " ".join(str(element) for element in label_class)

    return render_template('index.html', upload_image=upload_image, detect_image=detect_image, label_class=label_class, label_len=lebel_len)


if __name__ == '__main__':
    app.secret_key = "Your Key"
    app.run(host='0.0.0.0', port=5000)
