from flask import Flask, render_template, redirect, request, flash
import requests
import forex_python.converter as fx
from forex_python.converter import RatesNotAvailableError
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "Shahabcoding"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug=DebugToolbarExtension(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/result', methods=['POST'])
def get_data():
  
    first = request.form.get('old', '').upper()
    second = request.form.get('to', '').upper()
    amount = request.form.get('amount', '')
  
    if not first or not second or not amount:
      flash('Please enter a value for all fields')
      return redirect('/')

    try:
      fx.get_rate(first, second)
    except RatesNotAvailableError as e:
      flash(f'Error: {str(e)}')
      return redirect('/')
    
    url = f"https://api.exchangerate.host/convert?from={first}&to={second}&amount={amount}"
    response = requests.get(url)

    if response.status_code != 200:
      flash('Error in retreiving data')
      return redirect('/')

    data = response.json()
    converted_amount = round(data['result'], 2)
    return render_template('new.html', first= first, second=second, amount=amount, converted_amount=converted_amount)