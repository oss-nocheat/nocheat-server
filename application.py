from flask import Flask, request
from flask_socketio import SocketIO
from flask_cors import CORS
from Exam import Exam
from Student import Student

# Initialize flask app
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
# Initialize socket io
socketio = SocketIO(app, cors_allowed_origins="*")
# Connected student object list
clients = []
# Exam list
exams = []


# When client connected
@socketio.on('register')
def handle_connect(data):
    
    for student in clients:
        if student.session_id == request.sid:
            student.name = data['name']
            student.student_id = data['id']
            print(f'client regestered: {request.sid}')
            socketio.emit('success', {'id': id(student), 'message': f'client regestered: {id(student)}'},
                          sid=request.sid)
            break
    else:
        student = Student(request.sid, data['id'], data['name'])
        clients.append(student)
        socketio.emit('success', {'id': id(student), 'message': f'client regestered: {id(student)}'}, sid=request.sid)
        print(f'client regestered: {request.sid}')


@socketio.on('exam_join')
def join_session(data):
    
    client = find_client_by_socketid(clients, request.sid)
    print(client)
    if not client:
        print(f'client {request.sid} not found')
        socketio.emit('fail', {'message': f'client {request.sid} not found'}, sid=request.sid)
        return
    exam_id = data['examId']
    exam = find_exam_by_id(exams, exam_id)
    if exam:
        exam.examinee.append(client)
        socketio.emit('success', {'id': exam_id}, sid=request.sid)
        print(f'client {request.sid} regestered to exam {exam.name}')
        socketio.emit("exam_update")
        return
    else:
        socketio.emit('fail', {'message': f'exam {exam_id} not found'}, sid=request.sid)
        print(f'exam {exam_id} not found')
        return


@app.route('/client', methods=['GET'])
def get_clients():
    
    return {'result': [client.__dict__ for client in clients]}


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
    
    return {
        "result": [{'id': id(exam), 'name': exam.name, 'instructor': exam.instructor,
                    'examinee': str([item.name for item in exam.examinee])}
                   for exam in exams]}


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
        return {'result': [examinee.__dict__ for examinee in exam.examinee]}
    else:
        return {"message": "Entry not found"}, 404


@app.route('/exam/<exam_id>/join', methods=['POST'])
def join_exam(exam_id):
    
    exam = find_exam_by_id(exams, exam_id)
    if exam:
        json_data = request.json
        exam.examinee.append()
        socketio.emit("exam_update")
        return {"message": f'joined to {id(exam)}'}
    else:
        return {"message": "Entry not found"}, 404


def find_exam_by_id(exams, exam_id):
    
    print(exams)
    for exam in exams:
        print(f'{id(exam)} == {exam_id} | {id(exam) == exam_id}')
        if str(id(exam)) == exam_id:
            return exam


def find_client_by_socketid(clients, socket_id):
    
    for student in clients:
        if student.session_id == socket_id:
            return student


if __name__ == '__main__':
    socketio.run(app)
