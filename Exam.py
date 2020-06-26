class Exam:
    def __init__(self, instructor, name):
        
        self.name = name
        self.instructor = instructor
        self.examinee = []

        
    def add_examinee(self, examinee):
        
        self.examinee.append(examinee)
