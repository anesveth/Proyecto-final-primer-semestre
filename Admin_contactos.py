import sys, os

#lista
#directory =[{"Nombre":"asd", "Apellido":"Tomas", "Telefono":"443217"}]
UnorganizedDirectory = []

filename="InitialContacts.txt"
ProgramName="Admin_contactos.py"

def readfile(filename):
    '''reads contact list from InitialContacts.txt'''
    with open (filename) as archivo:
        return archivo.readlines()
        filename.close()

def loadcontacts(filename):
    '''loads contacts from file, has to be in same folder as the program'''
    PathOfFile=os.path.dirname(os.path.abspath(filename))
    PathOfProgram=os.path.dirname(os.path.abspath(ProgramName))
    if (PathOfFile==PathOfProgram):
        ReadingContacts=readfile(filename)
        data=[]
        for line in ReadingContacts:
            DataFromlist=line.split("\n")
            for j in DataFromlist:
                if j != "":
                    data.append(j)
        contacts=dict()
        for n in data:
            elements=n.split(",")
            try:
                contacts.update({"Nombre":str(elements[0]).strip(),"Apellido":str(elements[1]).strip(),"Telefono":str(elements[2]).strip()})
                UnorganizedDirectory.append(dict(contacts))
            except:
                contacts.update({"Nombre":str(elements[0]).strip(),"Apellido":"","Telefono":str(elements[1]).strip()})
                UnorganizedDirectory.append(dict(contacts))
        return UnorganizedDirectory
    else:
        return UnorganizedDirectory

def organizing_directory(UnorganizedDirectory):
    '''arranges contacts in alphabetical order by last name, all contacts without it are at the top'''
    loadcontacts(filename)
    UnorganizedDirectory=sorted(UnorganizedDirectory,key=lambda k:k["Apellido"])
    return (UnorganizedDirectory)

#se imprime de una buena manera
def pretty_print(directory, data = "all"):
    '''Prints the specified data (*default = "all") in dictionary'''
    #decidimos que datos imprimir
    if data == "all":
        print("---------Contactos---------")
        for contact in directory:
            print(" {}\t|| {}\t|| {}\t".format(contact["Nombre"], contact["Apellido"], contact["Telefono"]))


def initialize():
    '''declaration of basic variables'''
    directory=organizing_directory(UnorganizedDirectory)
    pretty_print(directory)
    main(directory)


#Controls program logic
def main(directory):
    '''runs the menu and sequence'''
    while(True):
        #opciones
        print("\n\n")
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
    #se obtiene el ultimo id, de lo contrario pasa como default 0
    if len(directory) > 0:
        contact_id = directory[len(directory)-1][id] + 1
    else:
        contact_id = 0
    new_contact = {"Id": contact_id, "Nombre":name, "Apellido":srname, "Telefono":phone, "Favorito":False}
    directory.append(new_contact)


def search_contact(directory, keys_searched, values_searched):
    '''searches contact by given list of keys and list of values, returns false if not finded'''
    Is_seached_contact = False
    #se compara cada contacto en directorio
    for contact_index in range(len(directory)):
        contact = directory[contact_index]
        Is_seached_contact = True
        #se compara con los datos especificados
        for i in range(len(keys_searched)):
            if(contact[keys_searched[i]] != values_searched[i]):
                Is_seached_contact = False
                break
        if Is_seached_contact:
            return contact
    return False

def call(contact_id):
    '''recieves id to make a call'''
    pass


#removes a contact
def remove_contact(directory, values_searched, keys_searched = ["Nombre"]):
    '''Searches the value(s) in all dictionarys in the given key(s) *key default = nombre\nkeys and values in a list'''
    contact = search_contact(directory, keys_searched, values_searched)
    if contact != False:
        directory.remove(contact)
        print("Eliminado exitosamente")
    else:
        print("No se encontro el contacto especificado")



#utilities
def clean():
    '''cleans the terminal'''
    os.system('cls||clear')
    print(":D\n")



#__init__
initialize()