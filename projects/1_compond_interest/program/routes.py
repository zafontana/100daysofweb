from flask import render_template
from program import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Template Demo')


@app.route('/compound_interest', methods=('GET', 'POST'))
def compound_interest():
    return render_template('compound_interest.html')
