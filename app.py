from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def form():
    return render_template('form.jinja')

@app.route('/', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f'Thank you for submitting the form, {name}! Your email is {email}.'

if __name__ == '__main__':
    app.run(debug=True)
