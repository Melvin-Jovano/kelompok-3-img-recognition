from flask import Flask, render_template, request
import os
import shutil
import uuid
from common.ai import preprocess, predict
from common.utils import getListDir

app = Flask(__name__, template_folder='templates', static_folder='public')

@app.template_filter('twodecimals')
def twodecimals(value):
    return "{:.2f}".format(value)

@app.route('/album')
def album():
    listDir = getListDir('public')
    albums = []

    for d in listDir:
        obj = {}
        obj['title'] = d.replace('_', ' ').title()
        obj['link'] = d
        albums.append(obj)

    return 'placeholder'

@app.route('/')
def form():
    return render_template('form.jinja')

@app.route('/', methods=['POST'])
def submit():
    for file in request.files.getlist('images'):
        if file.content_type.startswith('image/'):
            fileName = file.filename.split('.')
            img = str(uuid.uuid4()) + '.' + fileName[len(fileName) - 1]
            file.save(os.path.join('img', img))

    listDir = getListDir('img')

    res = predict(preprocess(listDir), listDir)

    for r in res:
        path = os.path.join('public', r["Predicted"][0][1])
        if not os.path.exists(path):
            os.mkdir(path)
        shutil.move(r["Image"], path)
    
    return render_template('result.jinja', result=res)

if __name__ == '__main__':
    app.run(debug=True)