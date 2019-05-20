"""
Functions to interact with http
"""
from data_from_file import add_contact
import requests

def get(directory, url):
    url = "http://demo7862839.mockable.io/contacts?gid=100"
    new_contacts = requests.get(url, gid=100).json()
    new_contacts = dict(new_contacts)
    for contact in new_contacts:
        add_contact(directory, contact["FirstName"], contact["LastName"], contact["Phone"] )

def put():
    pass