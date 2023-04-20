import click

# from app.Darasa import Darasa
from app.Student import Student

if __name__ == '__main__':

    @click.command()
    @click.option('--name', default='John', help='The student name')
    @click.option('--age', default=12, help='The student age')
    def create_student(name, age):
        student = Student(name, age)
        print(student.get_name())
        print(student.get_age())

    create_student()

    # # students = [Student("John", 12), Student("Jane", 13)]
    # dara = Darasa("Darasa la 7")
    # dara.add_student(Student("James", 14))
    #
    # for student in dara.get_students():
    #     print(student.name)
