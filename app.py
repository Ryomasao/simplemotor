from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="大人のモーター")


@app.route('/start')
def start_motor():
    return "start"


@app.route('/stop')
def stop_motor():
    return "stop"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
