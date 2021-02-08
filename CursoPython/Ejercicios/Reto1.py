# -*- coding: utf-8 -*-

def comparar(numero):
    
    numero.sort()

    if numero[0] == numero[1]:
        return 'Los números son Iguales'
    else:
        diferencia = numero[1] - numero[0]
        return 'El numero mayor es: '+ str(numero[1]) +', y su diferencia es: '+ str(diferencia)


if __name__ == '__main__':
    print('Compara dos números e indica si son iguales o cual es mayor y la diferencia entre los dos números')
    print(' ')
    num1 = int(input('Ingresa el primer numero a comparar: '))
    num2 = int(input('Ingresa el segundo numero a comparar: '))
    rta = comparar([num1, num2])
    print(' ')
    print(rta)
    
