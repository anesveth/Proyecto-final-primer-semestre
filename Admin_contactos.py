#---
import request
import os


#Controls program logic
def main():
    #lista
    directorio =[{"Nombre":"asd", "Apellido":"Tomas", "Telefono":"443217"}]
    #opciones
    print("Que quieres hacer?")
    print("1 - añadir contacto\n2 - remover contacto\n3 - Mostrar contactos")
    Answer = input()
    if Answer == 1:
        name = input("Ingresa el nombre: ")
        srname = input("Ingresa el apellido: ")
        phone = input("Ingresa el numero telefónico: ")
        add_contact(directorio, name, srname, phone)
    elif Answer == 2:
        remove_contact()
    elif Answer == 3:
        pretty_print(directorio)

#adds a contact
def add_contact(directorio, name, srname, phone):
    clean()



#removes a contact
def remove_contact():
    pass

#se imprime de una buena manera
def pretty_print(directorio, data = "all"):
    #decidimos que datos imprimir
    if data == "all":
        for contacto in directorio:
            print("Contactos")
            print(" {}\t|| {}\t|| {}\t".format(contacto["Nombre"], contacto["Apellido"], contacto["Telefono"]))



#utilities
def clean():
    os.system('cls||clear')
    print(":D\n")

