# -*- coding: utf-8 -*-

def foreig_exchange_calculator(ammount):
mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount


def run():
    print("Calculadora de Divisas")
    print("Convierte pesos Mexicanos a pesos Colombianos")
    print(" ")

    ammount = float(input('Ingresa la cantidad de pesos Mexicanos que quieres convertir: '))

    result = foreig_exchange_calculator(ammount)        
    print('${} pesos mexicanos son ${}'. format(ammount, result))
    print(' ')



if __name__ == '__main__':
    run()


