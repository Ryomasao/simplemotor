from flask import Flask
from flask import render_template
import dc_motor

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title="大人のモーター")


@app.route('/start')
def start_motor():
    dcmotor = dc_motor.DC_Motor_DRV8835(a_phase=14, a_enbl=15)
    dcmotor.start()
    return "start"


@app.route('/stop')
def stop_motor():
    dcmotor = dc_motor.DC_Motor_DRV8835(a_phase=14, a_enbl=15)
    dcmotor.stop()
    return "stop"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
