from flask import Flask,send_from_directory,jsonify
import os
from pathlib import Path


app = Flask(__name__)

ath = os.path.dirname(__file__)

nath = os.path.join(ath,'served_folder')

new = Path(nath)



@app.route('/')
def list_files():
    return jsonify(os.listdir(new))
   
@app.route('/files/<path:filename>')
def test(filename):
    return send_from_directory(new,filename)



if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 8080)