# -*- coding: utf-8 -*-

def func_decorador(func):
    def func_adicional(password):
        if password == 'platzi':
            return func()
        else:
            print('Contraseña incorrecta')

    return func_adicional    


@func_decorador  
def func_principal():
    print('Tu contraseña es correcta.')


if __name__ == '__main__':
    password = str(input('Ingresa la contraseña: '))

    func_principal(password)
