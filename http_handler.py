"""
Functions to interact with http
"""
from data_from_file import add_contact, get_json
import requests, json

def get_directory(directory, url, gid):
        '''gets contacts from json format in url to directory'''
        new_contacts = requests.get(url, params={"gid":gid}).json()
        for contact in new_contacts:
                try:
                        contact_name=contact["FirstName"]
                except:
                        contact_name=""
                try:
                        contact_srname=contact["LastName"]
                except:
                        contact_srname=""
                try:
                        contact_phone=contact["Phone"]
                except:
                        contact_phone=""

                add_contact(directory, contact_name, contact_srname, contact_phone)



def post_directory(directory, url, gid):
        '''posts the directory to the url in json format'''    
        data = get_json(directory)
        post = requests.post(url, data, params={"gid":gid})
        print (post)
    