#py libraries
import sys, os, time, msvcrt

#directory: {"Id": contact_id, "Nombre":name, "Apellido":srname, "Telefono":phone, "Favorito":False}

#global variables
UnorganizedDirectory = []
ProgramName="Admin_contactos.py"

#Loading data functions
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
        #spliting the lines by piece of data
        for line in ReadingContacts:
            DataFromlist=line.split("\n")
            for j in DataFromlist:
                if j != "":
                    data.append(j)
        for n in data:
            elements=n.split(",")
            #Tries to load every piece of data
            # //could try an if given the lenght of the list
            try:
                add_contact(UnorganizedDirectory, str(elements[0]).strip(),str(elements[1]).strip() , str(elements[2]).strip())
            except:
                try:
                    add_contact(UnorganizedDirectory, str(elements[0]).strip(),"" ,str(elements[1]).strip())
                except:
                    add_contact(UnorganizedDirectory, "","" ,str(elements[0]).strip())
        return UnorganizedDirectory
    else:
        return UnorganizedDirectory

def get_external_data(directory, filename =""):
    '''loads file and content of the given filename (should be in the same place as the code)'''
    try:
        directory=loadcontacts(filename)
    except:
        #no hay archivo
        pass
    return (directory)
    
#UI
def pretty_print(directory, data = "all", order = "by srname"):
    '''Prints the specified data (*default = "all") in dictionary in the specified order (*default = "by srname")'''
    #giving it the order
    if order == "by srname":
        ordered_directory = sort_dict_by_srname(directory)
    else:
        ordered_directory = directory
    #Deciding how data should be printed
    if data == "all":
        print("---------Contactos---------")
        for contact_no in range(len(ordered_directory)):
            contact = ordered_directory[contact_no]
            print(" {}\t|| {}\t|| {}\t|| {}\t".format(contact["Nombre"], contact["Apellido"], contact["Telefono"], contact["Id"]))
    elif data == "favorites":
        print("---------Contactos---------")
        for contact_no in range(len(ordered_directory)):
            contact = ordered_directory[contact_no]
            if contact["Favorito"]:
                print(" {}\t|| {}\t|| {}\t|| {}\t".format(contact["Nombre"], contact["Apellido"], contact["Telefono"], contact["Id"]))

def sort_dict_by_srname(directory):
    '''orders a list of dictionaries by the key "Apellido"'''
    directory=sorted(directory,key=lambda k:k["Apellido"])
    return (directory)

#Program logic sequence
def initialize():
    '''declaration of basic variables'''
    directory=get_external_data(UnorganizedDirectory, "InitialContacts.txt")
    pretty_print(directory)
    main(directory)

def main(directory):
    '''runs the menu and sequence'''
    while(True):
        #opciones
        print("\n\n")
        print("Que quieres hacer?")
        print("1 - Agregar contacto\n2 - Remover contacto\n3 - Mostrar contactos\n4 - Otros\n0 - Salir")
        Answer = input()
        clean()
        #Add contact
        if Answer == "1":
            name = input("Ingresa el nombre: ")
            srname = input("Ingresa el apellido: ")
            phone = input("Ingresa el numero telefónico: ")
            add_contact(directory, name, srname, phone)
        #remove contact
        elif Answer == "2":
            try:
                name = input("Ingresa el nombre: ")
                remove_contact(directory, [name], ["Nombre"])
            except:
                pass
        #show contacts
        elif Answer == "3":
            pretty_print(directory)
        #set to favorite
        elif Answer == "4":
            #not exseptions allowed// un tested zone
            clean()
            print("1 - Hacer favorito\n2 - Quitar favorito\n3 - Llamar\n4 - Mostrar favoritos\n5 - Enviar mensaje\n0 - volver")
            Answer = input()
            if Answer == "1":
                #not exseptions allowed
                change_contact(directory, input("Id del contacto: "), ["Favorito"], [True])
            #unset favorite
            elif Answer == "2":
                #not exseptions allowed
                change_contact(directory, input("Id del contacto: "), ["Favorito"], [False])
            elif Answer == "3":
                call_contact(directory, input("Id del contacto: "))
            elif Answer == "4":
                pretty_print(directory, "favorites")
            elif Answer == "5":
                send_message(directory)
            elif Answer == "0":
                pass
        elif Answer == "0":
            exit()
        else:
            print("Asegurate de ingresar el dato correcto")

#Editing directory
def add_contact(directory, name, srname, phone):
    '''puts given values in a dictionary and appends them in a list'''
    #se obtiene el ultimo id, de lo contrario pasa como default 1
    if len(directory) > 0:
        contact_id = directory[len(directory)-1]["Id"] + 1
    else:
        contact_id = 1
    new_contact = {"Id": contact_id, "Nombre":name, "Apellido":srname, "Telefono":phone, "Favorito":False}
    directory.append(new_contact)

def change_contact(directory, contact_id, keys_to_change, new_values):
    '''changes the given contact keys given to the new values'''
    for x in range(len(directory)):
        if str(directory[x]["Id"]) == contact_id:
            contacto = directory[x]
            try:
                contacto.update(zip(keys_to_change, new_values))
                return "succesful"
            except:
                return "keys or values wrong  "
    print("Id no encontrado")
    return "id not found"

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

def remove_contact(directory, values_searched, keys_searched = ["Nombre"]):
    '''Searches the value(s) in all dictionarys in the given key(s) *key default = nombre\nkeys and values in a list'''
    contact = search_contact(directory, keys_searched, values_searched)
    if contact != False:
        directory.remove(contact)
        print("Eliminado exitosamente")
    else:
        print("No se encontro el contacto especificado")

#functions
def call_contact(directory, contact_id):
    '''waits 60 secs or until "c" is pressed'''
    try:
        contact_id = int(contact_id)
        contact = search_contact(directory, ["Id"], [contact_id])
        print("Llamando a: {}\nTelefono: {}".format(contact["Nombre"], contact["Telefono"]))
        start_time = time.time()
        print("Presiona c para cancelar")
        while time.time() - start_time < 60:
            if msvcrt.kbhit():
                if msvcrt.getch() == b'c' or msvcrt.getch() == b'C':
                    break
        print("Llamada finalizada")
    except:
        print("Id invalido")
    
def send_message(directory):
    '''untested'''
    destinarios = []
    names = []
    #getting recipients
    while True:
        #getting id
        print("To: "+ str(names).replace(",", " "))
        id = input("Id destinario: ")
        try:
            id = int(id)
        except:
            pass
        contact = search_contact(directory, ["Id"], [id])
        if contact != False:
            #adding the recipient
            destinarios.append(contact)
            names.append(contact["Nombre"])
            print("\nTo: "+ str(names).replace(",", " ")+"\n")
            ans = input("Deseas agregar alguien mas (si/no): ").lower()
            while ans != "si" and ans != "no":
                ans = input("(si/no): ")
            if ans == "no":
                break   
        else: 
            print("Id incorrecto")
            pass
    print("\n\nTo: "+ str(names).replace(",", " "))
    message = input("Ingresa mensaje:\n")
    clean()
    print("\n\nTo: "+ str(names).replace(",", " "))
    print("Msg: "+ message)
    print("Mensaje enviado")
    
#Miscellaneous 
def clean():
    '''cleans the terminal'''
    os.system('cls||clear')
    print(":D\n")

#__init__
initialize()