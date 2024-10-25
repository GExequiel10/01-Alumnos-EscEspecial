import time
from rich.console import Console
from helpers.console_helpers import show_main, get_choice, clear_display
from controller.controller_students import ManageStudents

console = Console()


def main():
    manage = ManageStudents('students.json')

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
            students = manage.read_students()  # devuelve lista de alumnos
            print('---------------------------')
            if not students:
                print('No hay alumnos registrados')
            else:
                print('LISTA DE ALUMNOS:')
                for student in students:
                    print(
                        f'{student.name} {student.surname} - Multigrado:{student.multigrade}')
            print('---------------------------')

        elif choice == 3:
            name = input('Nombre del alumno para actualizar: ')
            surname = input('Apellido del alumno para actualizar: ')
            new_name = input('Correccion del nombre:')
            new_surname = input('Correccion del apellido:')
            new_multigrade = int(input('Nuevo Multigrado: '))
            manage.update_student(name, surname, new_name,
                                  new_surname, new_multigrade)

        elif choice == 4:
            name = input('Nombre del alumno que desea borrar: ')
            manage.delete_student(name)

        elif choice == 0:
            break
        else:
            console.print('Opcion incorrecta', style='bold red')
            console.print('Ingrese una opcion del 0-4:', style='bold red')
            time.sleep(2) # esta linea permite ver el mensaje de opcion incorrecta y luego limpia la pantalla


if __name__ == '__main__':
    main()
