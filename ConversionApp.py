from flask import Flask, render_template, request
from conversion_factors_dict import *

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

@app.route('/Convert1', methods=['POST'])
def convert1():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert1 = float(request.form['value_to_convert'])
            value_to_return1 = value_to_convert1*float(conv_factor['2'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return1=str(value_to_return1), value_to_convert1=str(value_to_convert1))

@app.route('/Convert2', methods=['POST'])
def convert2():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert2 = float(request.form['value_to_convert'])
            value_to_return2 = value_to_convert2*float(conv_factor['3'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return2=str(value_to_return2), value_to_convert2=str(value_to_convert2))

@app.route('/Convert3', methods=['POST'])
def convert3():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert3 = float(request.form['value_to_convert'])
            value_to_return3 = value_to_convert3*float(conv_factor['4'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return3=str(value_to_return3), value_to_convert3=str(value_to_convert3))

@app.route('/Convert4', methods=['POST'])
def convert4():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert4 = float(request.form['value_to_convert'])
            value_to_return4 = value_to_convert4*float(conv_factor['5'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return4=str(value_to_return4), value_to_convert4=str(value_to_convert4))

@app.route('/Convert5', methods=['POST'])
def convert5():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert5 = float(request.form['value_to_convert'])
            value_to_return5 = value_to_convert5*float(conv_factor['6'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return5=str(value_to_return5), value_to_convert5=str(value_to_convert5))

@app.route('/Convert6', methods=['POST'])
def convert6():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert6 = float(request.form['value_to_convert'])
            value_to_return6 = value_to_convert6*float(conv_factor['7'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return6=str(value_to_return6), value_to_convert6=str(value_to_convert6))

@app.route('/Convert7', methods=['POST'])
def convert7():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert7 = float(request.form['value_to_convert'])
            value_to_return7 = value_to_convert7*float(conv_factor['8'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return7=str(value_to_return7), value_to_convert7=str(value_to_convert7))

@app.route('/Convert8', methods=['POST'])
def convert8():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert8 = float(request.form['value_to_convert'])
            value_to_return8 = value_to_convert8*float(conv_factor['9'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return8=str(value_to_return8), value_to_convert8=str(value_to_convert8))

@app.route('/Convert9', methods=['POST'])
def convert9():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert9 = float(request.form['value_to_convert'])
            value_to_return9 = value_to_convert9*float(conv_factor['10'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return9=str(value_to_return9), value_to_convert9=str(value_to_convert9))

@app.route('/Convert10', methods=['POST'])
def convert10():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert10 = float(request.form['value_to_convert'])
            value_to_return10 = value_to_convert10*float(conv_factor['11'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return10=str(value_to_return10), value_to_convert10=str(value_to_convert10))

@app.route('/Convert11', methods=['POST'])
def convert11():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert11 = float(request.form['value_to_convert'])
            value_to_return11 = value_to_convert11*float(conv_factor['12'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return11=str(value_to_return11), value_to_convert11=str(value_to_convert11))

@app.route('/Convert12', methods=['POST'])
def convert12():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert12 = float(request.form['value_to_convert'])
            value_to_return12 = value_to_convert12*float(conv_factor['13'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return12=str(value_to_return12), value_to_convert12=str(value_to_convert12))

@app.route('/Convert13', methods=['POST'])
def convert13():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert13 = float(request.form['value_to_convert'])
            value_to_return13 = value_to_convert13*float(conv_factor['14'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return13=str(value_to_return13), value_to_convert13=str(value_to_convert13))

@app.route('/Convert14', methods=['POST'])
def convert14():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert14 = float(request.form['value_to_convert'])
            value_to_return14 = value_to_convert14*float(conv_factor['15'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return14=str(value_to_return14), value_to_convert14=str(value_to_convert14))

@app.route('/Convert15', methods=['POST'])
def convert15():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert15 = float(request.form['value_to_convert'])
            value_to_return15 = value_to_convert15*float(conv_factor['16'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return15=str(value_to_return15), value_to_convert15=str(value_to_convert15))

@app.route('/Convert16', methods=['POST'])
def convert16():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert16 = float(request.form['value_to_convert'])
            value_to_return16 = value_to_convert16*float(conv_factor['17'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return16=str(value_to_return16), value_to_convert16=str(value_to_convert16))

@app.route('/Convert17', methods=['POST'])
def convert17():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert17 = float(request.form['value_to_convert'])
            value_to_return17 = value_to_convert17*float(conv_factor['18'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return17=str(value_to_return17), value_to_convert17=str(value_to_convert17))

@app.route('/Convert18', methods=['POST'])
def convert18():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert18 = float(request.form['value_to_convert'])
            value_to_return18 = value_to_convert18*float(conv_factor['19'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return18=str(value_to_return18), value_to_convert18=str(value_to_convert18))

@app.route('/Convert19', methods=['POST'])
def convert19():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert19 = float(request.form['value_to_convert'])
            value_to_return19 = value_to_convert19*float(conv_factor['20'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return19=str(value_to_return19), value_to_convert19=str(value_to_convert19))

@app.route('/Convert20', methods=['POST'])
def convert20():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert20 = float(request.form['value_to_convert'])
            value_to_return20 = value_to_convert20*float(conv_factor['21'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return20=str(value_to_return20), value_to_convert20=str(value_to_convert20))

@app.route('/Convert21', methods=['POST'])
def convert21():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert21 = float(request.form['value_to_convert'])
            value_to_return21 = value_to_convert21*float(conv_factor['22'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return21=str(value_to_return21), value_to_convert21=str(value_to_convert21))

@app.route('/Convert22', methods=['POST'])
def convert22():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert22 = float(request.form['value_to_convert'])
            value_to_return22 = value_to_convert22*float(conv_factor['23'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return22=str(value_to_return22), value_to_convert22=str(value_to_convert22))

@app.route('/Convert23', methods=['POST'])
def convert23():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert23 = float(request.form['value_to_convert'])
            value_to_return23 = value_to_convert23*float(conv_factor['24'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return23=str(value_to_return23), value_to_convert23=str(value_to_convert23))

@app.route('/Convert24', methods=['POST'])
def convert24():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert24 = float(request.form['value_to_convert'])
            value_to_return24 = value_to_convert24*float(conv_factor['25'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return24=str(value_to_return24), value_to_convert24=str(value_to_convert24))

@app.route('/Convert25', methods=['POST'])
def convert25():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert25 = float(request.form['value_to_convert'])
            value_to_return25 = value_to_convert25*float(conv_factor['26'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return25=str(value_to_return25), value_to_convert25=str(value_to_convert25))

@app.route('/Convert26', methods=['POST'])
def convert26():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert26 = float(request.form['value_to_convert'])
            value_to_return26 = value_to_convert26*float(conv_factor['27'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return26=str(value_to_return26), value_to_convert26=str(value_to_convert26))

@app.route('/Convert27', methods=['POST'])
def convert27():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert27 = float(request.form['value_to_convert'])
            value_to_return27 = value_to_convert27*float(conv_factor['28'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return27=str(value_to_return27), value_to_convert27=str(value_to_convert27))

@app.route('/Convert28', methods=['POST'])
def convert28():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert28 = float(request.form['value_to_convert'])
            value_to_return28 = value_to_convert28*float(conv_factor['29'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return28=str(value_to_return28), value_to_convert28=str(value_to_convert28))

@app.route('/Convert29', methods=['POST'])
def convert29():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert29 = float(request.form['value_to_convert'])
            value_to_return29 = value_to_convert29*float(conv_factor['30'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return29=str(value_to_return29), value_to_convert29=str(value_to_convert29))

@app.route('/Convert30', methods=['POST'])
def convert30():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert30 = float(request.form['value_to_convert'])
            value_to_return30 = value_to_convert30*float(conv_factor['31'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return30=str(value_to_return30), value_to_convert30=str(value_to_convert30))

@app.route('/Convert31', methods=['POST'])
def convert31():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert31 = float(request.form['value_to_convert'])
            value_to_return31 = value_to_convert31*float(conv_factor['32'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return31=str(value_to_return31), value_to_convert31=str(value_to_convert31))

@app.route('/Convert32', methods=['POST'])
def convert32():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert32 = float(request.form['value_to_convert'])
            value_to_return32 = value_to_convert32*float(conv_factor['33'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return32=str(value_to_return32), value_to_convert32=str(value_to_convert32))

@app.route('/Convert33', methods=['POST'])
def convert33():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert33 = float(request.form['value_to_convert'])
            value_to_return33 = value_to_convert33*float(conv_factor['34'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return33=str(value_to_return33), value_to_convert33=str(value_to_convert33))

@app.route('/Convert34', methods=['POST'])
def convert34():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert34 = float(request.form['value_to_convert'])
            value_to_return34 = value_to_convert34*float(conv_factor['35'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return34=str(value_to_return34), value_to_convert34=str(value_to_convert34))

@app.route('/Convert35', methods=['POST'])
def convert35():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert35 = float(request.form['value_to_convert'])
            value_to_return35 = value_to_convert35*float(conv_factor['36'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return35=str(value_to_return35), value_to_convert35=str(value_to_convert35))

@app.route('/Convert36', methods=['POST'])
def convert36():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert36 = float(request.form['value_to_convert'])
            value_to_return36 = value_to_convert36*float(conv_factor['37'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return36=str(value_to_return36), value_to_convert36=str(value_to_convert36))

@app.route('/Convert37', methods=['POST'])
def convert37():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert37 = float(request.form['value_to_convert'])
            value_to_return37 = value_to_convert37*float(conv_factor['38'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return37=str(value_to_return37), value_to_convert37=str(value_to_convert37))

@app.route('/Convert38', methods=['POST'])
def convert38():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert38 = float(request.form['value_to_convert'])
            value_to_return38 = value_to_convert38*float(conv_factor['39'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return38=str(value_to_return38), value_to_convert38=str(value_to_convert38))

@app.route('/Convert39', methods=['POST'])
def convert39():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert39 = float(request.form['value_to_convert'])
            value_to_return39 = value_to_convert39*float(conv_factor['40'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return39=str(value_to_return39), value_to_convert39=str(value_to_convert39))

@app.route('/Convert40', methods=['POST'])
def convert40():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert40 = float(request.form['value_to_convert'])
            value_to_return40 = value_to_convert40*float(conv_factor['41'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return40=str(value_to_return40), value_to_convert40=str(value_to_convert40))

@app.route('/Convert41', methods=['POST'])
def convert41():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert41 = float(request.form['value_to_convert'])
            value_to_return41 = value_to_convert41*float(conv_factor['42'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return41=str(value_to_return41), value_to_convert41=str(value_to_convert41))

@app.route('/Convert42', methods=['POST'])
def convert42():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert42 = float(request.form['value_to_convert'])
            value_to_return42 = value_to_convert42*float(conv_factor['43'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return42=str(value_to_return42), value_to_convert42=str(value_to_convert42))

@app.route('/Convert43', methods=['POST'])
def convert43():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert43 = float(request.form['value_to_convert'])
            value_to_return43 = value_to_convert43*float(conv_factor['44'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return43=str(value_to_return43), value_to_convert43=str(value_to_convert43))

@app.route('/Convert44', methods=['POST'])
def convert44():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert44 = float(request.form['value_to_convert'])
            value_to_return44 = value_to_convert44*float(conv_factor['45'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return44=str(value_to_return44), value_to_convert44=str(value_to_convert44))

@app.route('/Convert45', methods=['POST'])
def convert45():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert45 = float(request.form['value_to_convert'])
            value_to_return45 = value_to_convert45*float(conv_factor['46'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return45=str(value_to_return45), value_to_convert45=str(value_to_convert45))

@app.route('/Convert46', methods=['POST'])
def convert46():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert46 = float(request.form['value_to_convert'])
            value_to_return46 = value_to_convert46*float(conv_factor['47'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return46=str(value_to_return46), value_to_convert46=str(value_to_convert46))

@app.route('/Convert47', methods=['POST'])
def convert47():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert47 = float(request.form['value_to_convert'])
            value_to_return47 = value_to_convert47*float(conv_factor['48'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return47=str(value_to_return47), value_to_convert47=str(value_to_convert47))

@app.route('/Convert48', methods=['POST'])
def convert48():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert48 = float(request.form['value_to_convert'])
            value_to_return48 = value_to_convert48*float(conv_factor['49'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return48=str(value_to_return48), value_to_convert48=str(value_to_convert48))

@app.route('/Convert49', methods=['POST'])
def convert49():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert49 = float(request.form['value_to_convert'])
            value_to_return49 = value_to_convert49*float(conv_factor['50'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return49=str(value_to_return49), value_to_convert49=str(value_to_convert49))

@app.route('/Convert50', methods=['POST'])
def convert50():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert50 = float(request.form['value_to_convert'])
            value_to_return50 = value_to_convert50*float(conv_factor['51'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return50=str(value_to_return50), value_to_convert50=str(value_to_convert50))

@app.route('/Convert51', methods=['POST'])
def convert51():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert51 = float(request.form['value_to_convert'])
            value_to_return51 = value_to_convert51*float(conv_factor['52'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return51=str(value_to_return51), value_to_convert51=str(value_to_convert51))

@app.route('/Convert52', methods=['POST'])
def convert52():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert52 = float(request.form['value_to_convert'])
            value_to_return52 = value_to_convert52*float(conv_factor['53'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return52=str(value_to_return52), value_to_convert52=str(value_to_convert52))

@app.route('/Convert53', methods=['POST'])
def convert53():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert53 = float(request.form['value_to_convert'])
            value_to_return53 = value_to_convert53*float(conv_factor['54'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return53=str(value_to_return53), value_to_convert53=str(value_to_convert53))

@app.route('/Convert54', methods=['POST'])
def convert54():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert54 = float(request.form['value_to_convert'])
            value_to_return54 = value_to_convert54*float(conv_factor['55'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return54=str(value_to_return54), value_to_convert54=str(value_to_convert54))

@app.route('/Convert55', methods=['POST'])
def convert55():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert55 = float(request.form['value_to_convert'])
            value_to_return55 = value_to_convert55*float(conv_factor['56'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return55=str(value_to_return55), value_to_convert55=str(value_to_convert55))

@app.route('/Convert56', methods=['POST'])
def convert56():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert56 = float(request.form['value_to_convert'])
            value_to_return56 = value_to_convert56*float(conv_factor['57'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return56=str(value_to_return56), value_to_convert56=str(value_to_convert56))

@app.route('/Convert57', methods=['POST'])
def convert57():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert57 = float(request.form['value_to_convert'])
            value_to_return57 = value_to_convert57*float(conv_factor['58'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return57=str(value_to_return57), value_to_convert57=str(value_to_convert57))

@app.route('/Convert58', methods=['POST'])
def convert58():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert58 = float(request.form['value_to_convert'])
            value_to_return58 = value_to_convert58*float(conv_factor['59'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return58=str(value_to_return58), value_to_convert58=str(value_to_convert58))

@app.route('/Convert59', methods=['POST'])
def convert59():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert59 = float(request.form['value_to_convert'])
            value_to_return59 = value_to_convert59*float(conv_factor['60'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return59=str(value_to_return59), value_to_convert59=str(value_to_convert59))

@app.route('/Convert60', methods=['POST'])
def convert60():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert60 = float(request.form['value_to_convert'])
            value_to_return60 = value_to_convert60*float(conv_factor['61'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return60=str(value_to_return60), value_to_convert60=str(value_to_convert60))

@app.route('/Convert61', methods=['POST'])
def convert61():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert61 = float(request.form['value_to_convert'])
            value_to_return61 = value_to_convert61*float(conv_factor['62'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return61=str(value_to_return61), value_to_convert61=str(value_to_convert61))

@app.route('/Convert62', methods=['POST'])
def convert62():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert62 = float(request.form['value_to_convert'])
            value_to_return62 = value_to_convert62*float(conv_factor['63'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return62=str(value_to_return62), value_to_convert62=str(value_to_convert62))

@app.route('/Convert63', methods=['POST'])
def convert63():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert63 = float(request.form['value_to_convert'])
            value_to_return63 = value_to_convert63*float(conv_factor['64'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return63=str(value_to_return63), value_to_convert63=str(value_to_convert63))

@app.route('/Convert64', methods=['POST'])
def convert64():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert64 = float(request.form['value_to_convert'])
            value_to_return64 = value_to_convert64*float(conv_factor['65'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return64=str(value_to_return64), value_to_convert64=str(value_to_convert64))

@app.route('/Convert65', methods=['POST'])
def convert65():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert65 = float(request.form['value_to_convert'])
            value_to_return65 = value_to_convert65*float(conv_factor['66'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return65=str(value_to_return65), value_to_convert65=str(value_to_convert65))

@app.route('/Convert66', methods=['POST'])
def convert66():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert66 = float(request.form['value_to_convert'])
            value_to_return66 = value_to_convert66*float(conv_factor['67'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return66=str(value_to_return66), value_to_convert66=str(value_to_convert66))

@app.route('/Convert67', methods=['POST'])
def convert67():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert67 = float(request.form['value_to_convert'])
            value_to_return67 = value_to_convert67*float(conv_factor['68'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return67=str(value_to_return67), value_to_convert67=str(value_to_convert67))

@app.route('/Convert68', methods=['POST'])
def convert68():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert68 = float(request.form['value_to_convert'])
            value_to_return68 = value_to_convert68*float(conv_factor['69'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return68=str(value_to_return68), value_to_convert68=str(value_to_convert68))

@app.route('/Convert69', methods=['POST'])
def convert69():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert69 = float(request.form['value_to_convert'])
            value_to_return69 = value_to_convert69*float(conv_factor['70'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return69=str(value_to_return69), value_to_convert69=str(value_to_convert69))

@app.route('/Convert70', methods=['POST'])
def convert70():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert70 = float(request.form['value_to_convert'])
            value_to_return70 = value_to_convert70*float(conv_factor['71'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return70=str(value_to_return70), value_to_convert70=str(value_to_convert70))

@app.route('/Convert71', methods=['POST'])
def convert71():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert71 = float(request.form['value_to_convert'])
            value_to_return71 = value_to_convert71*float(conv_factor['72'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return71=str(value_to_return71), value_to_convert71=str(value_to_convert71))

@app.route('/Convert72', methods=['POST'])
def convert72():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert72 = float(request.form['value_to_convert'])
            value_to_return72 = value_to_convert72*float(conv_factor['73'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return72=str(value_to_return72), value_to_convert72=str(value_to_convert72))

@app.route('/Convert73', methods=['POST'])
def convert73():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert73 = float(request.form['value_to_convert'])
            value_to_return73 = value_to_convert73*float(conv_factor['74'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return73=str(value_to_return73), value_to_convert73=str(value_to_convert73))

@app.route('/Convert74', methods=['POST'])
def convert74():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert74 = float(request.form['value_to_convert'])
            value_to_return74 = value_to_convert74*float(conv_factor['75'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return74=str(value_to_return74), value_to_convert74=str(value_to_convert74))

@app.route('/Convert75', methods=['POST'])
def convert75():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert75 = float(request.form['value_to_convert'])
            value_to_return75 = value_to_convert75*float(conv_factor['76'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return75=str(value_to_return75), value_to_convert75=str(value_to_convert75))

@app.route('/Convert76', methods=['POST'])
def convert76():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert76 = float(request.form['value_to_convert'])
            value_to_return76 = value_to_convert76*float(conv_factor['77'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return76=str(value_to_return76), value_to_convert76=str(value_to_convert76))

@app.route('/Convert77', methods=['POST'])
def convert77():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert77 = float(request.form['value_to_convert'])
            value_to_return77 = value_to_convert77*float(conv_factor['78'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return77=str(value_to_return77), value_to_convert77=str(value_to_convert77))

@app.route('/Convert78', methods=['POST'])
def convert78():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert78 = float(request.form['value_to_convert'])
            value_to_return78 = value_to_convert78*float(conv_factor['79'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return78=str(value_to_return78), value_to_convert78=str(value_to_convert78))

@app.route('/Convert79', methods=['POST'])
def convert79():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert79 = float(request.form['value_to_convert'])
            value_to_return79 = value_to_convert79*float(conv_factor['80'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return79=str(value_to_return79), value_to_convert79=str(value_to_convert79))

@app.route('/Convert80', methods=['POST'])
def convert80():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert80 = float(request.form['value_to_convert'])
            value_to_return80 = value_to_convert80*float(conv_factor['81'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return80=str(value_to_return80), value_to_convert80=str(value_to_convert80))

@app.route('/Convert81', methods=['POST'])
def convert81():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert81 = float(request.form['value_to_convert'])
            value_to_return81 = value_to_convert81*float(conv_factor['82'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return81=str(value_to_return81), value_to_convert81=str(value_to_convert81))

@app.route('/Convert82', methods=['POST'])
def convert82():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert82 = float(request.form['value_to_convert'])
            value_to_return82 = value_to_convert82*float(conv_factor['83'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return82=str(value_to_return82), value_to_convert82=str(value_to_convert82))

@app.route('/Convert83', methods=['POST'])
def convert83():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert83 = float(request.form['value_to_convert'])
            value_to_return83 = value_to_convert83*float(conv_factor['84'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return83=str(value_to_return83), value_to_convert83=str(value_to_convert83))

@app.route('/Convert84', methods=['POST'])
def convert84():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert84 = float(request.form['value_to_convert'])
            value_to_return84 = value_to_convert84*float(conv_factor['85'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return84=str(value_to_return84), value_to_convert84=str(value_to_convert84))

@app.route('/Convert85', methods=['POST'])
def convert85():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert85 = float(request.form['value_to_convert'])
            value_to_return85 = value_to_convert85*float(conv_factor['86'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return85=str(value_to_return85), value_to_convert85=str(value_to_convert85))

@app.route('/Convert86', methods=['POST'])
def convert86():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert86 = float(request.form['value_to_convert'])
            value_to_return86 = value_to_convert86*float(conv_factor['87'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return86=str(value_to_return86), value_to_convert86=str(value_to_convert86))

@app.route('/Convert87', methods=['POST'])
def convert87():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert87 = float(request.form['value_to_convert'])
            value_to_return87 = value_to_convert87*float(conv_factor['88'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return87=str(value_to_return87), value_to_convert87=str(value_to_convert87))

@app.route('/Convert88', methods=['POST'])
def convert88():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert88 = float(request.form['value_to_convert'])
            value_to_return88 = value_to_convert88*float(conv_factor['89'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return88=str(value_to_return88), value_to_convert88=str(value_to_convert88))

@app.route('/Convert89', methods=['POST'])
def convert89():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert89 = float(request.form['value_to_convert'])
            value_to_return89 = value_to_convert89*float(conv_factor['90'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return89=str(value_to_return89), value_to_convert89=str(value_to_convert89))

@app.route('/Convert90', methods=['POST'])
def convert90():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert90 = float(request.form['value_to_convert'])
            value_to_return90 = value_to_convert90*float(conv_factor['91'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return90=str(value_to_return90), value_to_convert90=str(value_to_convert90))

@app.route('/Convert91', methods=['POST'])
def convert91():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert91 = float(request.form['value_to_convert'])
            value_to_return91 = value_to_convert91*float(conv_factor['92'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return91=str(value_to_return91), value_to_convert91=str(value_to_convert91))

@app.route('/Convert92', methods=['POST'])
def convert92():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert92 = float(request.form['value_to_convert'])
            value_to_return92 = value_to_convert92*float(conv_factor['93'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return92=str(value_to_return92), value_to_convert92=str(value_to_convert92))

@app.route('/Convert93', methods=['POST'])
def convert93():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert93 = float(request.form['value_to_convert'])
            value_to_return93 = value_to_convert93*float(conv_factor['94'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return93=str(value_to_return93), value_to_convert93=str(value_to_convert93))

@app.route('/Convert94', methods=['POST'])
def convert94():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert94 = float(request.form['value_to_convert'])
            value_to_return94 = value_to_convert94*float(conv_factor['95'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return94=str(value_to_return94), value_to_convert94=str(value_to_convert94))

@app.route('/Convert95', methods=['POST'])
def convert95():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert95 = float(request.form['value_to_convert'])
            value_to_return95 = value_to_convert95*float(conv_factor['96'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return95=str(value_to_return95), value_to_convert95=str(value_to_convert95))

@app.route('/Convert96', methods=['POST'])
def convert96():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert96 = float(request.form['value_to_convert'])
            value_to_return96 = value_to_convert96*float(conv_factor['97'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return96=str(value_to_return96), value_to_convert96=str(value_to_convert96))

@app.route('/Convert97', methods=['POST'])
def convert97():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert97 = float(request.form['value_to_convert'])
            value_to_return97 = value_to_convert97*float(conv_factor['98'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return97=str(value_to_return97), value_to_convert97=str(value_to_convert97))

@app.route('/Convert98', methods=['POST'])
def convert98():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert98 = float(request.form['value_to_convert'])
            value_to_return98 = value_to_convert98*float(conv_factor['99'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return98=str(value_to_return98), value_to_convert98=str(value_to_convert98))

@app.route('/Convert99', methods=['POST'])
def convert99():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert99 = float(request.form['value_to_convert'])
            value_to_return99 = value_to_convert99*float(conv_factor['100'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return99=str(value_to_return99), value_to_convert99=str(value_to_convert99))

@app.route('/Convert100', methods=['POST'])
def convert100():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert100 = float(request.form['value_to_convert'])
            value_to_return100 = value_to_convert100*float(conv_factor['101'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return100=str(value_to_return100), value_to_convert100=str(value_to_convert100))

@app.route('/Convert101', methods=['POST'])
def convert101():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert101 = float(request.form['value_to_convert'])
            value_to_return101 = value_to_convert101*float(conv_factor['102'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return101=str(value_to_return101), value_to_convert101=str(value_to_convert101))

@app.route('/Convert102', methods=['POST'])
def convert102():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert102 = float(request.form['value_to_convert'])
            value_to_return102 = value_to_convert102*float(conv_factor['103'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return102=str(value_to_return102), value_to_convert102=str(value_to_convert102))

@app.route('/Convert103', methods=['POST'])
def convert103():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert103 = float(request.form['value_to_convert'])
            value_to_return103 = value_to_convert103*float(conv_factor['104'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return103=str(value_to_return103), value_to_convert103=str(value_to_convert103))

@app.route('/Convert104', methods=['POST'])
def convert104():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert104 = float(request.form['value_to_convert'])
            value_to_return104 = value_to_convert104*float(conv_factor['105'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return104=str(value_to_return104), value_to_convert104=str(value_to_convert104))

@app.route('/Convert105', methods=['POST'])
def convert105():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert105 = float(request.form['value_to_convert'])
            value_to_return105 = value_to_convert105*float(conv_factor['106'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return105=str(value_to_return105), value_to_convert105=str(value_to_convert105))

@app.route('/Convert106', methods=['POST'])
def convert106():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert106 = float(request.form['value_to_convert'])
            value_to_return106 = value_to_convert106*float(conv_factor['107'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return106=str(value_to_return106), value_to_convert106=str(value_to_convert106))

@app.route('/Convert107', methods=['POST'])
def convert107():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert107 = float(request.form['value_to_convert'])
            value_to_return107 = value_to_convert107*float(conv_factor['108'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return107=str(value_to_return107), value_to_convert107=str(value_to_convert107))

@app.route('/Convert108', methods=['POST'])
def convert108():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert108 = float(request.form['value_to_convert'])
            value_to_return108 = value_to_convert108*float(conv_factor['109'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return108=str(value_to_return108), value_to_convert108=str(value_to_convert108))

@app.route('/Convert109', methods=['POST'])
def convert109():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert109 = float(request.form['value_to_convert'])
            value_to_return109 = value_to_convert109*float(conv_factor['110'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return109=str(value_to_return109), value_to_convert109=str(value_to_convert109))

@app.route('/Convert110', methods=['POST'])
def convert110():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert110 = float(request.form['value_to_convert'])
            value_to_return110 = value_to_convert110*float(conv_factor['111'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return110=str(value_to_return110), value_to_convert110=str(value_to_convert110))

@app.route('/Convert111', methods=['POST'])
def convert111():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert111 = float(request.form['value_to_convert'])
            value_to_return111 = value_to_convert111*float(conv_factor['112'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return111=str(value_to_return111), value_to_convert111=str(value_to_convert111))

@app.route('/Convert112', methods=['POST'])
def convert112():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert112 = float(request.form['value_to_convert'])
            value_to_return112 = value_to_convert112*float(conv_factor['113'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return112=str(value_to_return112), value_to_convert112=str(value_to_convert112))

@app.route('/Convert113', methods=['POST'])
def convert113():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert113 = float(request.form['value_to_convert'])
            value_to_return113 = value_to_convert113*float(conv_factor['114'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return113=str(value_to_return113), value_to_convert113=str(value_to_convert113))

@app.route('/Convert114', methods=['POST'])
def convert114():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert114 = float(request.form['value_to_convert'])
            value_to_return114 = value_to_convert114*float(conv_factor['115'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return114=str(value_to_return114), value_to_convert114=str(value_to_convert114))

@app.route('/Convert115', methods=['POST'])
def convert115():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert115 = float(request.form['value_to_convert'])
            value_to_return115 = value_to_convert115*float(conv_factor['116'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return115=str(value_to_return115), value_to_convert115=str(value_to_convert115))

@app.route('/Convert116', methods=['POST'])
def convert116():
    if request.method == 'POST':
        if isfloat(request.form['value_to_convert']) == False:
            return render_template('index.html', conv_factor=conv_factor, error_message='Please enter a valid number')
        else:
            value_to_convert116 = float(request.form['value_to_convert'])
            value_to_return116 = value_to_convert116*float(conv_factor['117'][1])
            return render_template('index.html', conv_factor=conv_factor, value_to_return116=str(value_to_return116), value_to_convert116=str(value_to_convert116))

if __name__ == '__main__':
    app.run(debug=True)