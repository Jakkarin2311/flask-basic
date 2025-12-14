from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask - basic</title>
</head>
<body>
    <h1>Home Page</h1>
    <hr>
</body>
</html>
'''

@app.route('/<name>')
def show_name(name):
    return f'<h1>My name is {name}</h1>'

@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello, {name}</h1>'

@app.route('/greeting/<name>/<int:age>')
def greething(name, age):
    return f'<h1>My name is {name}. I am {age} years old.</h1>'

@app.route('/calculator/addition/<int:a>/<int:b>')
def addition(a, b):
    return f'<h1>{a} + {b} = {a + b}</h1>'

@app.route('/calculator/subtraction/<int:a>/<int:b>')
def addition(a, b):
    return f'<h1>{a} - {b} = {a - b}</h1>'

@app.route('/secretkey/<uuid:sk>')
def secretkey(sk):
    return f'my secret key is {sk}'

# if __name__ == '__main__':
#     app.run(debug=True)