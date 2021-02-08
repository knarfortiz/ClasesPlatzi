# -*- coding: utf-8 -*-
import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email



class ContactBook:

    def __init__(self):
        self._contacts = []


    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact) 
        self._save()


    def show_all(self):
        self._contador = 0
        for contact in self._contacts:
            self._print_contact(contact)
            self._contador = 1

        if self._contador == 0:
            self._msm('Lista vacia')


 
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
        else:
            self._msm('No encontrado')


    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._msm('No encontrado')


    def update(self, name):
        self.search(name)      
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                while True:
                    self._edit = str(input('''
            ¿Qué dato desea modificar?
            
            [n]ame
            [p]hone
            [e]mail
            [c]ancelar
                        ''')) 

                    if self._edit.lower() == 'n':
                        contact.name = str(input('Escribe el nuevo nombre: '))
                        self._save()
                        break
                    elif self._edit.lower() == 'p':
                        contact.phone = str(input('Escribe el nuevo teléfono: '))
                        self._save()
                        break
                    elif self._edit.lower() == 'e':
                        contact.email = str(input('Escribe el nuevo email: '))
                        self._save()
                        break 
                    elif self._edit.lower() == 'c':
                        break 
                    else:
                        print('Comando no encontrado')



    def _save(self):
        with open('contacts.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow( ('name', 'phone', 'email'))

            for contact in self._contacts:
                write.writerow( (contact.name, contact.phone, contact.email))


       
    def _print_contact(self, contact):
        print('-----------------------------------')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('-----------------------------------')


    def _msm(self, mensaje):
        print('--------------------')
        print(mensaje)
        print('--------------------')
        





















                

