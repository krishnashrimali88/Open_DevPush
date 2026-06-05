from flask import Flask

app = Flask(__name__)


@app.route('/rt')
def test():
    return 'hello'



app.run(host = '127.0.0.1',port = 8080)