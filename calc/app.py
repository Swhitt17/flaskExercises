from flask import Flask,request
from operations import add,sub,mult,div

app = Flask(__name__)


@app.route('/add')
def do_add():
    """Adds a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def do_sub():
    """Subtracts a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)


@app.route('/mult')
def do_mult():
    """Multiplies a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)


@app.route('/div')
def do_div():
    """Adds a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)

OPERATORS = {
    "add": add,
    "sub":sub,
    "mult": mult,
    "div":div 
}

@app.route('/math/<oper>')
def do_math(oper):
    """Do math on a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = OPERATORS[oper](a,b)
    return str(result)
