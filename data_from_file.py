import os, json
from contact_options import add_contact
#global variables
UnorganizedDirectory = []
ProgramName="Admin_contactos.py"
#Loading data functions
def readfile(filename):
    '''reads contact list from InitialContacts.txt or specified file'''
    with open (filename) as archivo:
        return archivo.readlines()
    filename.close()

def loadcontacts(filename):
    '''loads contacts from file, has to be in same folder as the program if it is InitialContacts.txt'''
    #############################
    #Used for InitialContacts.txt
    #############################
    if (filename =="InitialContacts.txt"):
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
    #############################
    #Used for when a file is uploaded from the menu
    #############################
    else:
        ReadingContacts=readfile(filename)
        data=[]
        #spliting the lines by piece of data
        for line in ReadingContacts:
            DataFromlist=line.split("\n")
            for j in DataFromlist:
                if j != "":
                    data.append(j)
        #proof that the formatting is correct
        n=str(data[1])
        formatting_requisite=n.count(",")
        if (formatting_requisite > 0):
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
            print("\n[Error] El formato de los contactos no es legible\n")

def load_from_file(directory, filename =""):
    '''loads file and content of the given filename (the opening file should be in the same place as the code)'''
    try:
        try:
            directory=loadcontacts(filename)
        except:
            #no hay archivo
            pass
        #InitialContacts was not found
        if (len(directory)>0):
            return directory
        else:
            return False
    #The file uploaded did not have the right formatting
    except:
        return False

def sort_dict_by_srname(directory):
    '''orders a list of dictionaries by the key "Apellido"'''
    directory=sorted(directory,key=lambda contact:contact["Apellido"])
    return (directory)

def get_json(directory):
    '''returns a json with contacts inside, keys are FirstName, LastName and Phone'''
    json_directory = []
    for contact in directory:
        print(contact)
        json_contact = {"FirstName":contact["Nombre"], "LastName":contact["Apellido"], "Phone":contact["Telefono"]}
        json_directory.append(json_contact)
    return json_directory


    