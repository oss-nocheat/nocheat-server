from flask import Flask, render_template
from flask_socketio import SocketIO

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


class StudentClient:
    def __init__(self, socket_id):
        self.socket_id = socket_id


if __name__ == '__main__':
    socketio.run(app)

