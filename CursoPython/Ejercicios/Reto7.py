# -*- coding: utf-8 -*-

MSJ = {
    1:'Hoy aprenderemos sobre prorgamación',
    2:'¿Qué tal tomar un curso de marketing digital?',
    3:'Hoy es un gran día para comenzar a aprender de diseño',
    4:'¿Y si aprendemos algo de negocios online?',
    5:'Veamos un par de clases sobre producción audiovisual',
    6:'Tal vez sea bueno desarrollar una habilidad blanda en Platzi'
    }

if __name__ == '__main__':
    while True: 
        num = int(input('Ingresa un numero entre 1 y 6: '))
        print(" ")
        if num in MSJ:
            print(MSJ[num])
            break
        else:
            print("Ingresa un numero correcto!!")
            print(" ")
 
