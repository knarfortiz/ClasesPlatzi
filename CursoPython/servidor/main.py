# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')


def hola_mundo():
    return'Hola, mis perros'


if __name__ == '__main__':
    app.run()
