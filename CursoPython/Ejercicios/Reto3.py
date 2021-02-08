# -*- coding: utf-8 -*-
def comparar(num1, num2, num3):
    if num1 > num2:
        if num1 > num3 and num2 < num3:
            return 'El número '+ str(num3) +' se encuentra en el rango, gracias'
        elif num1 < num3:
            return 'El número '+ str(num3) +' excede el límite superior'
        else:
            return 'El número '+ str(num3) +' excede el límite inferior'
    else: 
        return 'No sea mk, coloque bien el rango'


if __name__ == '__main__':
    num1 = int(input('Ingrese el # limite superior: '))
    num2 = int(input('Ingrese el # limite inferior: '))
    num3 = int(input('Ingrese el # a comparar: '))
    rta = comparar(num1, num2, num3)
    print('')
    print(rta)   
