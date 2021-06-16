from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from time import sleep
from threading import Thread, Event


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

thread = Thread()
thread_stop_event = Event()

EMULATE_HX711 = True
if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def get_data():
    hx = HX711(5, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(308)
    hx.reset()
    hx.tare()
    print("Tare done! Add weight now...")

    num_of_objects = 0
    last_value = 0
    while not thread_stop_event.isSet():

        val = hx.get_weight(5)

        if val > last_value:
            if 30 <= abs(val - last_value) <= 75:
                # print "Difference: %d" % (val - last_value)
                num_of_objects += 1
                last_value = val
        elif last_value > val:
            if 30 <= abs(last_value - val):
                num_of_objects = max(0, num_of_objects - 1)
                last_value = val

        print("Sensors values: %s" % val)
        print("Number of objects: %s" % num_of_objects)
        print("__________________________________")

        hx.power_down()
        hx.power_up()

        number = str(val) + ',' + str(num_of_objects)

        socketio.emit('newnumber', {'number': number}, namespace='/test')
        socketio.sleep(5)


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(get_data)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)