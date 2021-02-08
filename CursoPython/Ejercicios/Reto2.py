# -*- coding: utf-8 -*-
def comparar(num1, num2):
    if num1 > num2:
        return 'El número '+ str(num2) +' se encuentra en el rango, gracias'
    else:
        return 'El número '+ str(num2) +' excede el límite permitido'


if __name__ == '__main__':
    num1 = int(input('Ingrese el # limite: '))
    num2 = int(input('Ingrese el # a comparar: '))
    rta = comparar(num1, num2)
    print('')
    print(rta)   
