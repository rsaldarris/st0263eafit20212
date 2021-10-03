import time
import os
from crobject import CRObject
from dbobjects import DBObjects
from prettytable import PrettyTable

db = DBObjects()


def print_options():
    print('Proyecto 1 \n')
    print('Selecciona una opción:')
    print('1. Crear objeto')
    print('2. Listar objetos')
    print('3. Modificar objeto')
    print('4. Eliminar objeto')
    print('5. Buscar objeto')
    print('6. Salir')


def run():
    print_options()

    print('Que desea hacer?')
    command = input('Escriba aqui el numero de la opcion: ')

    if command == '1':
        create_crobject()
    elif command == '2':
        list_crobjects()
    elif command == '3':
        edit_crobject()
    elif command == '4':
        delete_crobject()
    elif command == '5':
        search_crobject()
    elif command == '6':
        os._exit(1)
    else:
        print('Comando inválido')
        time.sleep(1)

    run()


def create_crobject():
    print('\n Crear objeto')
    while True:
        key = input("Escribe un numero entero como key: ")
        try:
            key = int(key)
            break
        except ValueError:
            print("La key es incorrecta: escribe un numero entero")

    while True:
        value = input("Escribe el valor que deseas almacenar: ")
        try:
            value = str(value)
            break
        except ValueError:
            print("El valor es incorrecto escribelo de nuevo")

    crobject = CRObject(None, key, value)
    if db.save_crobject(crobject):
        print('Objeto insertado con éxito')
    else:
        print('Error al guardar el objeto')


def list_crobjects():
    list_crobjects = db.list_crobjects()

    if not list_crobjects:
        return print('Todavía no hay objetos guardados')

    table = PrettyTable(db.get_schema().keys())
    for crobject in list_crobjects:
        table.add_row([
            crobject.getid(),
            crobject.getkey(),
            crobject.getvalue(),
        ])

    print(table)
    print('Pulsa intro para salir')
    command = input()


def search_crobject():

    filter = {}
    
    print('Introduce una key ')
    crkey = input('->')
    # filter['KEY'] = crkey

    try:
        list_crobjects = db.search_crobjects(crkey)
        if not list_crobjects:
            return print('No hay ningún objeto con ese criterio de búsqueda')

        _print_table_crobjects(list_crobjects)
    except ValueError as err:
        print(err)
        time.sleep(1)
        search_crobject()


def _print_table_crobjects(list_crobjects):
    table = PrettyTable(db.get_schema().keys())
    for crobject in list_crobjects:
        table.add_row([
            crobject.getid(),
            crobject.getkey(),
            crobject.getvalue(),
        ])

    print(table)
    print('Pulsa cualquier tecla para continuar')
    command = input()


def edit_crobject():
    list_crobjects()
    data = {}

    while True:
        print('Introduce la key')
        key = input('Key: ')
        print('Y el value:')
        value = input('Value:')
        print('Y el nuevo value:')
        nvalue = input('Value:')
        try:
            data['KEY'] = key
            data['VALUE'] = nvalue
            break
        except ValueError:
            print("El valor es incorrecto escribelo de nuevo")

    try:
        res = db.update(key, value, data)
        if res:
            print('Objeto actualizado con éxito')
    except Exception:
        print('Hubo un error, intentalo de nuevo')
        time.sleep(1)
        edit_crobject()


def delete_crobject():
    list_crobjects()
    key,value = getInput()
        
    try:
        res = db.delete(key,value)
        if res:
            print('Contacto eliminado con éxito')
    except Exception:
        print('Hubo un error, intentalo de nuevo')
        time.sleep(1)
        delete_crobject()

def getInput():
    while True:
        key = input("Escribe un numero entero como key: ")
        try:
            key = int(key)
            break
        except ValueError:
            print("La key es incorrecta: escribe un numero entero")

    while True:
        value = input("Escribe el valor: ")
        try:
            value = str(value)
            break
        except ValueError:
            print("El valor es incorrecto escribelo de nuevo")

    return key,value


if __name__ == "__main__":
    run()
