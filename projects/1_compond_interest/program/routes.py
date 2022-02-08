from flask import render_template, request
from program import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Template Demo')


@app.route('/compound_interest', methods=('GET', 'POST'))
def compound_interest(gap=None, monthly_deposit=None):
    if request.method == 'POST':
        goal = float(request.form.get('goal'))
        initial_amount = float(request.form.get('initial_amount'))
        monthly_rate = float(request.form.get('monthly_rate'))
        monthly_rate /= 100  # make it a percentage
        months = int(request.form.get('months'))

        # calculate future value of initial amount
        future_value = initial_amount*(pow((1+monthly_rate), months))

        # gap that needs to contribute to
        gap = goal - future_value

        # calculate monthly deposits
        monthly_deposit = gap / ((monthly_rate + 1) ** months - 1) * monthly_rate

        return render_template('compound_interest.html', monthly_deposit=monthly_deposit)
    else:
        return render_template('compound_interest.html')
