from flask import render_template
from program import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Template Demo')


@app.route('/compound_interest')
def p100days():
    return render_template('compound_interest.html')
