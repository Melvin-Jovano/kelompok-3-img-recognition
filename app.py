from flask import Flask, render_template, request
import os
import shutil
import uuid
from common.ai import preprocess, predict

app = Flask(__name__, template_folder='templates')

@app.route('/')
def form():
    return render_template('form.jinja')

@app.route('/', methods=['POST'])
def submit():
    # imgList = []
    for file in request.files.getlist('images'):
        if file.content_type.startswith('image/'):
            fileName = file.filename.split('.')
            img = str(uuid.uuid4()) + '.' + fileName[len(fileName) - 1]
            file.save(os.path.join('img', img))
            # imgList.append(img)
    res = predict(preprocess(os.listdir("img")), os.listdir("img"))
    for r in res:
        path = os.path.join('public', r["Predicted"][0][1])
        if not os.path.exists(path):
            os.mkdir(path)
        shutil.move(r["Image"], path)
    
    return 'Files uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)