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

if __name__ == '__main__':
    app.run(debug=True)