import sys, os
from data_from_file import UnorganizedDirectory, sort_dict_by_srname, get_external_data, add_contact
#functions that handle the directory (adding contacts and uploading them from a file)
from contact_options import change_contact,search_contact,remove_contact,call_contact,send_message
#functions that handle the contacts in the directory (modifying, deleting, searching, etc.); 
# also all the options from the extra menu

#directory: {"Id": contact_id, "Nombre":name, "Apellido":srname, "Telefono":phone, "Favorito":False}   
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
        print("｡o°✥✤✣ Contactos ✣✤✥°o｡")
        for contact_no in range(len(ordered_directory)):
            contact = ordered_directory[contact_no]
            print(" {}\t|| {}\t|| {}\t|| {}\t".format(contact["Nombre"], contact["Apellido"], contact["Telefono"], contact["Id"]))
    elif data == "favorites":
        print("｡o°✥✤✣ Contactos Favoritos ✣✤✥°o｡")
        for contact_no in range(len(ordered_directory)):
            contact = ordered_directory[contact_no]
            if contact["Favorito"]:
                print(" {}\t|| {}\t|| {}\t|| {}\t".format(contact["Nombre"], contact["Apellido"], contact["Telefono"], contact["Id"]))

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
            print("Intentalo de nuevo, y asegurate de ingresar el dato correcto")

 #Miscellaneous 
def clean():
    '''cleans the terminal'''
    os.system('cls||clear')
    print("✼　 ҉ 　✼　 ҉ 　✼　 ҉ 　✼　 ҉ 　✼　 ҉ 　✼\n")

#__init__
initialize()