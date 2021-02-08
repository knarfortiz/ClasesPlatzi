# -*- coding: utf-8 -*-
import random
import os


def main():
    control = 1
    while control == 1:
        os.system('clear')
        print('')
        print('***************************************************************')
        print('Adivina el número !!!, debes ingresar el rango de los numeros')
        print('---------------------------------------------------------------')
        intentos = 0
        minimo = int(input('Ingrese el menor numero: '))
        maximo = int(input('Ingrese el maximo numero: '))
        random_number = random.randint(minimo, maximo)
        print('')
        print('El rango seleccionado es [{}:{}]'.format(minimo, maximo))
        print('---------------------------------------------------------------')
        print('')

        number_found = False
        while not number_found:
            intentos += 1
            if intentos <= 5:
                number = int(input('Intenta un número: '))

                if number == random_number:
                    print('---------------------------------------------------------------')
                    #print('Correcto care nalga :v') Un programador serio no imprime eso
                    print('Estimado usuario, el numero escogido es correcto :v')
                    control = int(input('Deseas volver a jugar? Si(1) o No(0): ')) 
                    print('')
                    print('')
                    number_found = True
                    intentos = 0
            else:
                print('---------------------------------------------------------------')
                print('Intentos máximos alcanzados :( !!!')
                control = int(input('Deseas volver a jugar? Si(1) o No(0): ')) 
                print('')
                print('')
                intentos = 0
                break


if __name__ == '__main__':
    main()
