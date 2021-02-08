# -*- coding: utf-8 -*-

def mensajes(edad):
    if edad >= 30:
        print("Nunca es tarde para aprender ¿Qué curso tomaremos?.")
    elif edad > 18 and edad < 29:
        print("Es un momento excelente para impulsar tu carrera.")
    else:
        print("¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.")

if __name__ == '__main__':
    edad = int(input('Ingrese su edad: '))
    mensajes(edad)
