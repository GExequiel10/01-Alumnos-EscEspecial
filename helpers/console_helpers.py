import os
import time # importe time para que la consola no quedara constanmente llena de informacion

# importe la libreria rich para darle color al CRUD
from rich.console import Console

# creo una instancia de Console para poder imprimir en color, segun la documentacion de pypi
console = Console()


def clear_display():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def show_main():
    # creo el menu del CRUD
    console.print('>>> MENU <<<', style='bold green')
    console.print('1.Agregar Alumno:', style='yellow')
    console.print('2.Leer Alumnos:', style='yellow')
    console.print('3.Actualizar Alumno:', style='yellow')
    console.print('4.Borrar Alumno:', style='yellow')
    console.print('0.Salir:', style='yellow')


def get_choice():
    while True:
        clear_display()
        show_main()
        try:
            return int(input('Ingrese una opcion: '))
        except ValueError:
            console.print(
                'Ingrese una opcion válida (solo numeros del 0-4):', style='bold red')
            time.sleep(2)
