from flask import Flask, request, render_template, redirect, flash, jsonify
from currency import get_amt, currency_symbol, check_curr_validity
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/conversion', methods=['POST'])
def conv_page():
    bcurr = request.form['bcurr']
    tcurr = request.form['tcurr']
    amt = float(request.form['amt'])
    arr = []

    if amt < 0:
        arr.append("Enter a positive amount")

    if not check_curr_validity(bcurr):
        arr.append(f"Not a valid base currency: {bcurr}")

    if not check_curr_validity(tcurr):
        arr.append(f"Not a valid target currency: {tcurr}")

    if arr:
        for items in arr:
            msg = flash(items)
        return render_template("home.html", msg=msg)

    else:
        symb = currency_symbol(tcurr)
        converted_amt = get_amt(bcurr, tcurr, amt)
        return render_template("converted.html", symb=symb, converted_amt=converted_amt)