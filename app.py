# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from flask import Flask, request, redirect, url_for, render_template, send_from_directory,flash 
from werkzeug.utils import secure_filename
import cv2
import config
import os
import glob
from Engine import maskIdentifier

UPLOAD_FOLDER =config.UPLOAD_FOLDER
DOWNLOAD_FOLDER = config.DOWNLOAD_FOLDER
ALLOWED_EXTENSIONS = {'jpg', 'png','.jpeg'}
app = Flask(__name__, static_url_path="/static")


# APP CONFIGURATIONS
app.config['SECRET_KEY'] = 'opencv'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 6mb
app.config['MAX_CONTENT_LENGTH'] = 6 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def cleaner(directory):
    if len(os.listdir(directory)) != 0:
        files = glob.glob(directory+'*')
        for f in files:
            os.remove(f)
    else:    
        pass
    
# @app.route('/webcam',methods=['POST'])
# def Home():
#     return render_template('WebSnapshot.html')

@app.route('/',methods=['GET'])
def Home2():
    return render_template('index.html')

@app.route('/Bot', methods=['POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            cleaner(config.UPLOAD_FOLDER)
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            image,_=maskIdentifier(filename).mask_image()
            cleaner(config.DOWNLOAD_FOLDER)
            cv2.imwrite(config.DOWNLOAD_FOLDER+filename,image)
            data={
                "processed_img":config.DOWNLOAD_FOLDER+filename,
                "uploaded_img":config.UPLOAD_FOLDER+filename
            }
            return render_template("index.html",data=data)  
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
