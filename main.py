from flask import Flask, request
from fractions import Fraction
import json
import decimal
import statistics
from decimal import Decimal
app = Flask(__name__)

@app.route('/')
def index():
    #return 'Usage;\nOperation?X=<Value1>\n' api syntax failed for single vector operand
    if request.method == 'GET':
        value1 = request.args.get('X', default=0, type=str)

    else:
        value1 = request.values.get('X', default=0, type=str)
    try:
        value1 = [Fraction(value) for value in value1.split(',')]
    except ValueError:
        error = "error, enter proper input"
        return error

    return value1
@app.route('/average')
@app.route('/mean')
@app.route('/avg')
def mean():
    try:
        value1 = index()
        result = sum(value1) / len(value1)
    except ValueError:
        error = index()
        return error
    else:
        if float(result).is_integer():#to avoid unsuported operand types
            result = int(result)
            return result
        return str(float(result))

@app.route('/max')
def maximum():
    try:
        value1 = index()
        result = max(value1)
    except ValueError:
        error = index()
        return error
    else:
        if float(result).is_integer():#to avoid unsuported operand types
            answer = int(result)
            return "%d" % result
        return str(float(round(result)))

@app.route('/median')
def median():
    try:
        value1 = index()
        result = statistics.median(value1)
    except ValueError:
        error = index()
        return error
    else:
        if float(result).is_integer():#to avoid unsuported operand types
            result = "%d" % result
            return result
        return str(float(result))

@app.route('/min')
def minimum():
    try:
        value1 = index()
        result = min(value1)
    except ValueError:
        error = index()
        return error
    else:
        if float(result).is_integer():#to avoid unsuported operand types
            answer = int(result)
            return "%d" % result
        return str(float(round(result)))

if __name__ == "__main__":
    app.run()
