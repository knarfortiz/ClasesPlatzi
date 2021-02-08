# -*- coding: utf-8 -*-

def verificar(animal):
    f_animal = animal.lower()

    if f_animal == 'tortuga':
        return True
    else:
        return False


if __name__ == '__main__':
    animal = str(input('Ingresa tu animal favorito: '))
    rta = verificar(animal)
    print('')
    if rta:
        print('También me gustan las tortugas')
    else:
        print('Ese animal es genial, pero prefiero las tortugas')
