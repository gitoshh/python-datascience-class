class Darasa:
    def __init__(self, name, all_students=None):
        if all_students is None:
            all_students = []
        self.students = all_students
        self.name = name

    def get_students(self):
        return self.students

    def add_student(self, new_student):
        self.students.append(new_student)

