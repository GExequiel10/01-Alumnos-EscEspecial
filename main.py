from rich import console
from helpers.console_helpers import show_main, get_choice
from controller.controller_students import ManageStudents


def main():
    Manage = ManageStudents('students.json')

    while True:
        show_main()
        choice = get_choice()

        if choice == 1:
            name = input('Nombre de alumno:')
            multigrade = int(input('Multigrado al que pertenece(del 1-10):'))
            Manage.add_student(name, multigrade)

        elif choice == 2:
            students = Manage.read_students()
            print('---------------------------')
            print('Lista de alumnos:')
            if not students:
                print('No hay alumnos registrados')

            else:
                for student in students:
                    print(
                        f'Nombre:{student.name}, Multigrado:{student.multigrade}')
            print('---------------------------')

        elif choice == 3:
            name = input('Nombre del alumno para actualizar: ')
            new_name = input('Correccion del nombre:')
            new_multigrade = int(input('Nuevo Multigrado: '))
            Manage.update_student(name, new_name, new_multigrade)

        elif choice == 4:
            name = input('Nombre del alumno que desea borrar: ')
            Manage.delete_student(name)

        elif choice == 0:
            break
        else:
            print('Opcion incorrecta')


if __name__ == '__main__':
    main()
