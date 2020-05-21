from flask import Flask, render_template
from flask_socketio import SocketIO
from StudentClient import StudentClient

# initialize flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# initialize socket io
socketio = SocketIO(app, cors_allowed_origins="*")
# connected student object list
student_clients = list()


# when client connected
@socketio.on('message')
def handle_client_connect(data):
    print(f'client {data} connected')
    student_clients.append(StudentClient(data))


@app.route('/')
def index():
    return '''
    hello world!
    '''

@app.route('/play_sample')
def play_sample():
    socketio.emit('play')

if __name__ == '__main__':
    socketio.run(app)

