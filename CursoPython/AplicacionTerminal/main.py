# -*- coding: utf-8 -*-

# from Clases.agenda import ContactBook

import sys
sys.path.append('./Clases') 
from agenda import * 


def run():
    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contactos
            [ac]tualizar contacto
            [b]buscar contacto
            [e]liminar contacto 
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            print('Añadir contacto')
            name = str(input('Escribe el nombre del contacto: ')) 
            phone = str(input('Escribe el tel del contacto: ')) 
            email = str(input('Escribe el email del contacto: ')) 

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('Actualiar contacto')
            name = str(input('Escribe el nombre del contacto: ')) 
            contact_book.update(name)

        elif command == 'b':
            #print('Buscar contacto')
            name = str(input('Escribe el nombre del contacto: ')) 
            contact_book.search(name)

        elif command == 'e':
            #print('Eliminar contacto')
            name = str(input('Escribe el nombre del contacto: ')) 
            contact_book.delete(name) 

        elif command == 'l':
            #print('Listar contacto')
            contact_book.show_all()

        elif command == 's':
            break

        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print(' ')
    print('Bienvenido')
    run()
