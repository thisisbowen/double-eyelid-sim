import os
from flask import Flask, request, redirect, url_for, flash, Response,render_template
from werkzeug.utils import secure_filename
from processing import process_image
import datetime
import time
import random



now = datetime.datetime.now()
UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(microseconds=1)
app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#TREATMENT GROUP
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'pic.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('result'))
        #if request.form["action"] == "Process":
        #    file = process_image('uploads/test_image1.jpg')
        #    filename = secure_filename(file.filename)
        #    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #    return redirect(url_for('result'))
        #return redirect(url_for('result'))

    return render_template('web/home.html')

@app.route('/show_result', methods=['GET', 'POST'])
def result():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if process_image('uploads/pic.jpg') == None:
        flash('抱歉，您上传的图片无法识别。请重新上传一张新的正脸照片。')
        return redirect(url_for('upload_file'))
    else:
        return render_template('web/result.html')

#CONTROL GROUP 1
@app.route('/cg1', methods=['GET', 'POST'])
def cg1_upload_file():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'pic.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg1_result'))
        if request.form["action"] == "Process":
            file = process_image('uploads/test_image1.jpg')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg1_result'))
        return redirect(url_for('cg1_result'))
    return render_template('web/cg1_home.html')

@app.route('/cg1_show_result')
def cg1_result():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    #time.sleep(random.randint(5,10))
    if process_image('uploads/pic.jpg') == None:
        flash('抱歉，您上传的图片无法识别。请重新上传一张新的正脸照片。')
        return redirect(url_for('cg1_upload_file'))
    else:
        return render_template('web/cg1_result.html')

#CONTROL GROUP 2
@app.route('/cg2', methods=['GET', 'POST'])
def cg2_upload_file():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'pic.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg2_result'))
        if request.form["action"] == "Process":
            file = process_image('uploads/test_image1.jpg')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg2_result'))
        return redirect(url_for('cg2_result'))
    return render_template('web/cg2_home.html')

@app.route('/cg2_show_result')
def cg2_result():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    #time.sleep(random.randint(5,10))
    if process_image('uploads/pic.jpg') == None:
        flash('抱歉，您上传的图片无法识别。请重新上传一张新的正脸照片。')
        return redirect(url_for('cg2_upload_file'))
    else:
        return render_template('web/cg2_result.html')

#CONTROL GROUP 3
@app.route('/cg3', methods=['GET', 'POST'])
def cg3_upload_file():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'pic.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg3_result'))
        if request.form["action"] == "Process":
            file = process_image('uploads/test_image1.jpg')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg3_result'))
        return redirect(url_for('cg3_result'))
    return render_template('web/cg3_home.html')

@app.route('/cg3_show_result')
def cg3_result():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    #time.sleep(random.randint(5,10))
    if process_image('uploads/pic.jpg') == None:
        flash('抱歉，您上传的图片无法识别。请重新上传一张新的正脸照片。')
        return redirect(url_for('cg3_upload_file'))
    else:
        return render_template('web/cg3_result.html')

#CONTROL GROUP 4
@app.route('/cg4', methods=['GET', 'POST'])
def cg4_upload_file():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'pic.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg4_result'))
        if request.form["action"] == "Process":
            file = process_image('uploads/test_image1.jpg')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg4_result'))
        return redirect(url_for('cg4_result'))
    return render_template('web/cg4_home.html')

@app.route('/cg4_show_result')
def cg4_result():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    #time.sleep(random.randint(5,10))
    if process_image('uploads/pic.jpg') == None:
        flash('抱歉，您上传的图片无法识别。请重新上传一张新的正脸照片。')
        return redirect(url_for('cg4_upload_file'))
    else:
        return render_template('web/cg4_result.html')

#CONTROL GROUP 5
@app.route('/cg5', methods=['GET', 'POST'])
def cg5_upload_file():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'pic.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg5_result'))
        if request.form["action"] == "Process":
            file = process_image('uploads/test_image1.jpg')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg5_result'))
        return redirect(url_for('cg5_result'))
    return render_template('web/cg5_home.html')

@app.route('/cg5_show_result')
def cg5_result():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    #time.sleep(random.randint(5,10))
    if process_image('uploads/pic.jpg') == None:
        flash('抱歉，您上传的图片无法识别。请重新上传一张新的正脸照片。')
        return redirect(url_for('cg5_upload_file'))
    else:
        return render_template('web/cg5_result.html')

#CONTROL GROUP 6
@app.route('/cg6', methods=['GET', 'POST'])
def cg6_upload_file():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'pic.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg6_result'))
        if request.form["action"] == "Process":
            file = process_image('uploads/test_image1.jpg')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('cg6_result'))
        return redirect(url_for('cg6_result'))
    return render_template('web/cg6_home.html')

@app.route('/cg6_show_result')
def cg6_result():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    #time.sleep(random.randint(5,10))
    if process_image('uploads/pic.jpg') == None:
        flash('抱歉，您上传的图片无法识别。请重新上传一张新的正脸照片。')
        return redirect(url_for('cg6_upload_file'))
    else:
        return render_template('web/cg6_result.html')


#BASELINE GROUP
@app.route('/bg', methods=['GET', 'POST'])
def bg_upload_file():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'pic.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('bg_result'))
        if request.form["action"] == "Process":
            file = process_image('uploads/test_image1.jpg')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('bg_result'))
        return redirect(url_for('bg_result'))
    return render_template('web/bg_home.html')

@app.route('/bg_show_result')
def bg_result():
    try:
        os.remove('static/input.jpg')
        os.remove('static/output.jpg')
        os.remove('uploads/pic.jpg')
    except FileNotFoundError:
        pass
    #time.sleep(random.randint(5,10))
    if process_image('uploads/pic.jpg') == None:
        flash('抱歉，您上传的图片无法识别。请重新上传一张新的正脸照片。')
        return redirect(url_for('bg_upload_file'))
    else:
        return render_template('web/bg_result.html')

#CONTROL GROUP
if __name__ == '__main__':
	app.run(debug=True)

