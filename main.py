from flask import Flask, request
from flask_socketio import SocketIO
from flask_cors import CORS
from Exam import Exam
from Student import Student

# initialize flask app
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
# initialize socket io
socketio = SocketIO(app, cors_allowed_origins="*")
# connected student object list
clients = list()
# exam list
exams = []


# when client connected
@socketio.on('register')
def handle_connect(data):
    for student in clients:
        if student.session_id == request.sid:
            socketio.send({'id': id(student)}, sid=request.sid)
            return
    else:
        student = Student(request.sid, data['id'], data['name'])
        clients.append(student)
        socketio.send({'id': id(student)}, sid=request.sid)
    print(request.sid)
    print(clients)


@app.route('/')
def index():
    return '''
    hello world!
    '''


@app.route('/play_sample')
def play_sample():
    socketio.emit('play', [[392.00, 1000],
                           [392.00, 1000],
                           [440, 1000],
                           [440, 1000],
                           [392.00, 1000],
                           [392.00, 1000],
                           [329.63, 1000]])
    return 'sample played'


@app.route('/exam', methods=['POST'])
def create_exam():
    json_data = request.json
    instructor = json_data['instructor']
    name = json_data['name']

    if not (instructor and name):
        return {"message": "Insufficient data"}, 400
    exam = Exam(instructor, name)
    exams.append(exam)
    socketio.emit("exam_update")
    return {'id': id(exam)}


@app.route('/exam', methods=['GET'])
def get_exams():
    return {"result": [{'id': id(exam), 'name': exam.name, 'instructor': exam.instructor} for exam in exams]}


@app.route('/exam/<exam_id>', methods=['GET'])
def get_exam(exam_id):
    exam = find_exam_by_id(exams, exam_id)
    if exam:
        return exam.__dict__
    else:
        return {"message": "Entry not found"}, 404


@app.route('/exam/<exam_id>/examinees', methods=['GET'])
def get_examinees(exam_id):
    exam = find_exam_by_id(exams, exam_id)
    if exam:
        return exam['examinees']
    else:
        return {"message": "Entry not found"}, 404


@app.route('/exam/<exam_id>/join', methods=['POST'])
def join_exam(exam_id):
    exam = find_exam_by_id(exams, exam_id)

    if exam:
        json_data = request.json
        exam.examinee.append()
    else:
        return {"message": "Entry not found"}, 404


def find_exam_by_id(exams, id):
    for exam in exams:
        if id(exam) == id:
            return exam


if __name__ == '__main__':
    socketio.run(app)
