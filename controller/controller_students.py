import json

from rich.console import Console

console = Console()

class Student:
    def __init__(self, name, surname, multigrade):
        self.name = name
        self.surname = surname
        self.multigrade = multigrade


class ManageStudents:
    def __init__(self, file):
        self.file = file
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.file, 'r') as f:
                return [Student(student['Nombre'], student['Apellido'], student['Multigrado'])for student in json.load(f)]
        except:
            return []

    def save_students(self):
        student_data = []
        for student in self.students:
            student_data.append(
                {'Nombre': student.name, 'Apellido': student.surname, 'Multigrado': student.multigrade})
        with open(self.file, 'w') as f:
            json.dump(student_data, f)

    def add_student(self, name, surname, multigrade):
        self.students.append(Student(name, surname, multigrade))
        self.save_students()

    def read_students(self):
        return self.students

    def update_student(self, name, surname, new_name, new_surname, new_multigrade):
        for student in self.students:
            if student.name == name and student.surname == surname:
                student.name = new_name
                student.surname = new_surname
                student.multigrade = new_multigrade
                self.save_students()
                console.print('Alumno encontrado y actualizado', style='bold blue')
                return
        console.print('Alumno no encontrado', style='bold orange')

    def delete_student(self, name, surname):
        for student in self.students:
            if student.name == name and student.surname == surname:
                self.students.remove(student)
                self.save_students()
                print('Alumno encontrado y borrado')
                return
        print('Alumno no encontrado(for)')
