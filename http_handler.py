"""
Functions to interact with http
"""
from data_from_file import add_contact, get_json
import requests, json

def get_directory(directory, url, gid):
    url = "http://demo7862839.mockable.io/contacts?gid=100"
    new_contacts = requests.get(url, params={"gid":gid}).json()
    new_contacts = json.loads(new_contacts)
    for contact in new_contacts:
        add_contact(directory, contact["FirstName"], contact["LastName"], contact["Phone"] )

def post_directory(directory, url, gid):
    data = get_json(directory)
    requests.post(url, data, params={"gid":gid})
    