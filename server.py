from flask import Flask,send_from_directory
import os
from pathlib import Path
app = Flask(__name__)

ath = os.path.dirname(__file__)

nath = os.path.join(ath,'served_folder')

new = Path(nath)
print(nath)


@app.route('/')
def list_files():
    files = os.listdir(new)
    return '<br>'.join(f'<a href="/files/{f}">{f}</a>' for f in files)

@app.route('/files/<path:filename>')
def test(filename):
    return send_from_directory(new,filename)



if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 8080)