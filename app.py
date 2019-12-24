from pathlib import Path
from flask import Flask, request, redirect, render_template, url_for, send_from_directory
from utils import add_time,is_file_allow
from model import run_model

app = Flask(__name__)

dir_path = Path('.')
upload_path = str(dir_path/'static'/'uploads')

content_filename, style_filename = '',''

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/upload",methods=['GET','POST'])

def upload():
    if request.method=='POST':
        content_image =request.files['content']
        style_image = request.files['style']

        content_filename = add_time(content_image.filename)
        style_filename = add_time(style_image.filename)

        if is_file_allow(content_filename):
            content_image.save(upload_path+'/'+content_filename)

        if is_file_allow(style_filename):
            style_image.save(upload_path+'/'+style_filename)

        else:
            print("File is not supported. Please see the extension. Allowed: png, jpeg, jpg")
            return url_for('home')
        
        return render_template('upload.html',content=content_filename,style=style_filename)

@app.route('/upload/<filename>')
def serve_image(filename):
    return send_from_directory(directory='static/uploads',filename=filename)

@app.route('/model',methods=['GET','POST'])
def style_tranfer():

    if request.method=='POST':
        output_filename=run_model(content=content_filename,style=style_filename,folder=upload_path)
        print(f'Output Filename: {output_filename}')
        return render_template('model.html', output_image=output_filename)

if __name__ == "__main__":
    app.run(debug=True)
