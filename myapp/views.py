from flask import Flask, flash, render_template, redirect, url_for
from myapp.model import GenerateForm
from myapp.password import Password

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

@app.route('/', methods = ['GET', 'POST'])
def index():

    form = GenerateForm()
    password = Password(12)
    if form.validate_on_submit():
        flash(password.generateFullPassword())
        return redirect(url_for('index')) 
    return render_template('index.html', form = form)

