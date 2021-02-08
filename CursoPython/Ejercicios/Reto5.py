# -*- coding: utf-8 -*-

def clima(rta_lluvia_m):
    if rta_lluvia_m == 'si':
        rta_viento = str(input('Esta haciendo mucho viento? (si / no): '))
        rta_viento_m = rta_viento.lower()

        if rta_viento_m == 'si':
            print('Hace mucho viento para salir con una sombrilla')
        else:
            print('Lleve una sombrilla')
    else:
        print('Que tenga un bonito día')


if __name__ == '__main__':
    rta_lluvia = str(input('Esta lloviendo? (si / no): '))
    rta_lluvia_m = rta_lluvia.lower()
    clima(rta_lluvia_m)
                        
