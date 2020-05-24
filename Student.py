class Student:
    def __init__(self, session_id, student_id, name):
        self.session_id = session_id
        self.student_id = student_id
        self.name = name
        self.adjacent_students = []
