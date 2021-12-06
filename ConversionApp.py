from flask import Flask, render_template, request
from conversion_factors_dict import *
from decimal import Decimal

app = Flask(__name__)

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

@app.route('/')
def index():
    return render_template('index.html', conv_factor=conv_factor)

@app.route("/Convert", methods=['POST'])
def convert():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert = float(request.form['value_to_convert'])
            value_to_return = value_to_convert*float(conv_factor[str(request.form['factor_id'])][1])
            factor_id = str(request.form['factor_id'])
            value_to_return_dict = {}
            value_to_convert_dict = {}
            value_to_return_dict[factor_id] = str(value_to_return)
            value_to_convert_dict[factor_id] = str(value_to_convert)
            return render_template('index.html', conv_factor=conv_factor, **locals())

if __name__ == '__main__':
        app.run(debug=True)