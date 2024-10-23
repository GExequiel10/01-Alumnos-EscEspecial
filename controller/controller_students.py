import json


class Student:
    def __init__(self, name, multigrade):
        self.name = name
        self.multigrade = multigrade


class ManageStudents:
    def __init__(self, file):
        self.file = file
        self.students = self.load_students()

    def load_students(self):
        # if not self.file.endswitch('.json'):
        #     return []

        # with open(self.file, 'r') as f:
        #     data = json.load(f)

        # students = []
        # for student in data:
        #     new_student = Student(student('Nombre'), student['Multigrado'])
        #     students.append(new_student)

        # return students
        try:
            with open(self.file, 'r') as f:
                return [Student(student('nombre'), student['Multigrado'])for student in json.load(f)]
        except:
            return []

    def save_students(self):
        student_data = []
        for student in self.students:
            student_data.append(
                {'Nombre': student.name, 'Multigrado': student.multigrade})
        with open(self.file, 'w') as f:
            json.dump(student_data, f)

    def add_student(self, name, multigrade):
        self.students.append(Student(name, multigrade))
        self.save_students()

    def read_students(self):
        for student in self.students:
            print(f'Nombre: {student.name} Multigrado {student.multigrade}')

    def update_student(self, name, new_name, new_multigrade):
        for student in self.students:
            if student.name == name:
                student.name = new_name
                student.multigrade = new_multigrade
                self.save_students()
                return
            print('Alumno encontrado y actualizado')

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                self.save_students()
                return
            print('Alumno encontrado y borrado')
