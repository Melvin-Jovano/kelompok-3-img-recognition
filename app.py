from flask import Flask, render_template, request
import os
import uuid

app = Flask(__name__, template_folder='templates')

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
    
    return 'Files uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)