import json
import time
from rich.console import Console
from helpers.console_helpers import show_main, get_choice, clear_display

console = Console()


class TodoStudents:

    @classmethod
    def start(cls):
        manage = ManageStudents('students.json')

        def show_students():  # metodo de instancia
            students = manage.read_students()
            print('---------------------------')
            if not students:
                print('No hay alumnos registrados')
                time.sleep(3)
                return False
            else:
                print('LISTA DE ALUMNOS:')
                for student in students:
                    print(
                        f'Multigrado:{student.multigrade} - {student.name} {student.surname}')
                print('---------------------------')
                return True

        while True:
            clear_display()
            show_main()
            choice = get_choice()

            if choice == 1:
                name = input('Nombre de alumno:')
                surname = input('Apellido:')
                try:
                    multigrade = int(
                        input('Multigrado al que pertenece(del 1-10):'))
                    if multigrade < 1 or multigrade > 10:
                        console.print(
                            'El multigrado no existe. Ingrese un Multigrado del 1-10:', style='orange')
                        continue
                except ValueError:
                    console.print(
                        'Por favor, ingrese un multigrado del 1-10', style='orange')
                    continue
                manage.add_student(name, surname, multigrade)

            elif choice == 2:
                show_students()
                time.sleep(3)

            elif choice == 3:
                if not show_students():
                    return  # o continue???
                name = input('Nombre del alumno para actualizar: ')
                surname = input('Apellido del alumno para actualizar: ')
                new_name = input('Correccion del nombre:')
                new_surname = input('Correccion del apellido:')
                new_multigrade = int(input('Nuevo Multigrado: '))
                manage.update_student(name, surname, new_name,
                                      new_surname, new_multigrade)
                console.print('Datos del alumno actualizado',
                              style='bold green')
                time.sleep(3)

            elif choice == 4:
                if not show_students():
                    continue  # o return???
                name = input('Nombre del alumno que desea borrar: ')
                surname = input('Apellido del alumno que desea borrar: ')
                manage.delete_student(name, surname)
                time.sleep(3)

            elif choice == 0:
                break
            else:
                console.print('Opcion incorrecta', style='bold red')
                console.print('Ingrese una opcion del 0-4:', style='bold red')
                # esta linea permite ver el mensaje de opcion incorrecta y luego limpia la pantalla
                time.sleep(2)


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
                console.print('Alumno encontrado y actualizado',
                              style='bold blue')
                return
        console.print('Alumno no encontrado', style='bold orange')

    def delete_student(self, name, surname):
        for student in self.students:
            if student.name == name and student.surname == surname:
                self.students.remove(student)
                self.save_students()
                print('Alumno encontrado y borrado')
                return
        print('Alumno no encontrado')
