#---
import request
import os

def initialize():
    '''declaration of basic variables'''
    #lista
    #directory =[{"Nombre":"asd", "Apellido":"Tomas", "Telefono":"443217"}]
    directory = []
    main(directory)


#Controls program logic
def main(directory):
    '''runs the menu and sequence'''
    while(True):
        #opciones
        print("\n\n\n")
        print("Que quieres hacer?")
        print("1 - añadir contacto\n2 - remover contacto\n3 - Mostrar contactos\n0 - salir")
        Answer = input()
        clean()
        if Answer == "1":
            name = input("Ingresa el nombre: ")
            srname = input("Ingresa el apellido: ")
            phone = input("Ingresa el numero telefónico: ")
            add_contact(directory, name, srname, phone)
        elif Answer == "2":
            try:
                name = input("Ingresa el nombre: ")
                remove_contact(directory, [name], ["Nombre"])
            except:
                pass
        elif Answer == "3":
            pretty_print(directory)
        elif Answer == "0":
            exit()
        else:
            print("Asegurate de ingresar el dato correcto")
#adds a contact
def add_contact(directory, name, srname, phone):
    '''puts given values in a dictionary and appends them in a list'''
    new_contact = {"Nombre":name, "Apellido":srname, "Telefono":phone}
    directory.append(new_contact)


#removes a contact
def remove_contact(directory, values_searched, keys_searched = ["Nombre"]):
    '''Searches the value(s) in all dictionarys in the given key(s) *key default = nombre\nkeys and values in a list'''
    Is_seached_contact = False
    #se compara cada contacto en directorio
    for contact in directory:
        Is_seached_contact = True
        #se compara con los datos especificados
        for i in range(len(keys_searched)):
            if(contact[keys_searched[i]] != values_searched[i]):
                Is_seached_contact = False
                break
        if Is_seached_contact:
            directory.remove(contact)
            break   
    if Is_seached_contact:
        print("Eliminado exitosamente")
    else:
        print("No se encontro el contacto especificado")

#se imprime de una buena manera
def pretty_print(directory, data = "all"):
    '''Prints the specified data (*default = "all") in dictionary'''
    #decidimos que datos imprimir
    if data == "all":
        print("Contactos")
        for contact in directory:
            print(" {}\t|| {}\t|| {}\t".format(contact["Nombre"], contact["Apellido"], contact["Telefono"]))

#utilities
def clean():
    '''cleans the terminal'''
    os.system('cls||clear')
    print(":D\n")



#__init__
initialize()