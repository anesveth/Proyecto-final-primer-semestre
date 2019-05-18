import time, sys
def change_contact(directory, contact_id, keys_to_change, new_values):
    '''changes the given contact keys to the new values'''
    for x in range(len(directory)):
        if str(directory[x]["Id"]) == contact_id:
            contacto = directory[x]
            try:
                contacto.update(zip(keys_to_change, new_values))
                return "succesful"
            except:
                return "keys or values wrong  "
    print("Id no encontrado :(")
    return False

def search_contact(directory, keys_searched, values_searched):
    '''searches contact by given list of keys and list of values, returns false if not found'''
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
    '''Searches the value(s) in the dictionaries of the directory by the given key(s) *key default = nombre.
    Keys and values in a list'''
    contact = search_contact(directory, keys_searched, values_searched)
    if contact != False:
        directory.remove(contact)
        print("Eliminado exitosamente ｡.｡:+*")
    else:
        print("No se encontro el contacto especificado :(")

def call_contact(directory, contact_id):
    '''calls for 60 secs or until "c" is pressed'''
    try:
        contact_id = int(contact_id)
    except:
        print("Id invalido :(")
    contact = search_contact(directory, ["Id"], [contact_id])
    if contact != False :
        print("Llamando a: {} {}\nTelefono: {}".format(contact["Nombre"], contact["Apellido"], contact["Telefono"]))
        start_time = time.time()
        print("Presiona c para cancelar")
        while time.time() - start_time < 60:
            if msvcrt.kbhit():
                if msvcrt.getch() == b'c' or msvcrt.getch() == b'C':
                    break
        print("*+:｡.｡ Llamada finalizada ｡.｡:+*")
    else:
        print ("Id invalido")

    
def send_message(directory):
    '''sends message to chosen contact(s)'''
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
            ans = input("Deseas agregar alguien mas? (si/no): ").lower()
            while ans != "si" and ans != "no":
                ans = input("(si/no): ")
            if ans == "no":
                break   
        else: 
            print("Id incorrecto")
            pass
    print("\n\nTo: "+ str(names).replace(",", " "))
    message = input("Ingresa mensaje:\n")
    print("\n\nTo: "+ str(names).replace(",", " "))
    
    print("Msg: "+ message)
    print("Mensaje enviado ｡.｡:+*")