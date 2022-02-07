if you can't find the flask app on windows, try setting it with:
` $env:FLASK_APP="demo.py"`
not sure what's going on here. worked the first day, didn't the second (maybe forgot to launch pycharm as admin?).

## To Do:
- figure out why python-dotenv is not working

Tomorrow: continue with forms


## On compound interest:
From https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
>The formula for compound interest, including principal sum, is:
>A = P(1 + r/n)^(nt)
>Where:
>
>A = the future value of the investment/loan, including interest
>P = the principal investment amount (the initial deposit or loan amount)
>r = the annual interest rate (decimal)
>n = the number of times that interest is compounded per unit t
>t = the time the money is invested or borrowed for

I'm using n=1 for the time being, so the formula becomes `A=P(1+r)^t`


## Other references
- https://python-adv-web-apps.readthedocs.io/en/latest/flask_forms.html#introduction