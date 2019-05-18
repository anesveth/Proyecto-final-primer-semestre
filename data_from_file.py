import os
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

def sort_dict_by_srname(directory):
    '''orders a list of dictionaries by the key "Apellido"'''
    directory=sorted(directory,key=lambda k:k["Apellido"])
    return (directory)


#Editing directory
def add_contact(directory, name, srname, phone):
    '''puts given values in a dictionary and appends them to the directory list'''
    #se obtiene el ultimo id, de lo contrario pasa como default 1
    if len(directory) > 0:
        contact_id = directory[len(directory)-1]["Id"] + 1
    else:
        contact_id = 1
    new_contact = {"Id": contact_id, "Nombre":name, "Apellido":srname, "Telefono":phone, "Favorito":False}
    directory.append(new_contact)