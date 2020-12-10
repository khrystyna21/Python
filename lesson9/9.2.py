

"""
    Functionality of Phonebook application:
    Add new entries
    Search by first name
    Search by last name
    Search by full name
    Search by telephone number
    Search by city or state
    Delete a record for a given telephone number
    Update a record for a given telephone number
    An option to exit the program
    The first argument to the application should be the name of the phonebook.
        Application should load JSON data, if it is present in the folder with application,
        else raise an error. After the user exits, all data should be saved to loaded JSON.
"""
import json
import os
from typing import List, Dict

file_name = input("Type phonebook name: ")
phonebook = json.load(open(file_name))


def add_new_entry(phonebook: List[Dict[str, str]]) -> bool:
    print('Adding new entry: ')
    firstname = input('First name: ')
    secondname = input('Second name: ')
    lastname = input('Last name: ')
    phone = input('Phone: ')
    city = input('City: ')
    phonebook.append({
        'first_name': firstname,
        'last_name': lastname,
        'second_name': secondname,
        'phone': phone,
        'city': city
    })
    return True

def search_by_first_name(phonebook: List[Dict[str, str]]) -> None:
    os.system('clear')
    result = None
    while True:
        required_name = input('Type First name to search for: ')
        for item in phonebook:
            if item['first_name'] == required_name:
                result = item
        if result is None:
            choice = input('Nothing, found, repeat? y/n ')
            if choice != 'y':
                break
            else:
                continue
        print('Item found: ', result)
        input('enter to exist')
        break

def search_by_last_name(phonebook: List[Dict[str, str]]) -> None:
    os.system('clear')
    result = None
    while True:
        required_name = input('Type Last name to search for: ')
        for item in phonebook:
            if item['last_name'] == required_name:
                result = item
        if result is None:
            choice = input('Nothing, found, repeat? y/n ')
            if choice != 'y':
                break
            else:
                continue
        print('Item found: ', result)
        input('enter to exist')
        break


def search_by_full_name(phonebook: List[Dict[str, str]]) -> None:
    os.system('clear')
    result = None
    while True:
        required_last_name = input('Type Last name to search for: ')
        required_first_name = input('Type First name to search for: ')
        required_second_name = input('Type Second name to search for: ')
        for item in phonebook:
            if item['last_name'] == required_last_name \
                    and item['first_name'] == required_first_name \
                    and item['second_name'] == required_second_name :
                result = item
        if result is None:
            choice = input('Nothing, found, repeat? y/n ')
            if choice != 'y':
                break
            else:
                continue
        print('Item found: ', result)
        input('enter to exist')
        break

def search_by_city(phonebook: List[Dict[str, str]]) -> None:
    os.system('clear')
    result = None
    while True:
        required_city = input('Type city to search for: ')
        for item in phonebook:
            if item['city'] == required_city:
                result = item
        if result is None:
            choice = input('Nothing, found, repeat? y/n ')
            if choice != 'y':
                break
            else:
                continue
        print('Item found: ', result)
        input('enter to exist')
        break

def search_by_phone(phonebook: List[Dict[str, str]]) -> None:
    os.system('clear')
    result = None
    while True:
        required_phone = input('Type phone number to search for: ')
        for item in phonebook:
            if item['phone'] == required_phone:
                result = item
        if result is None:
            choice = input('Nothing, found, repeat? y/n ')
            if choice != 'y':
                break
            else:
                continue
        print('Item found: ', result)
        input('enter to exist')
        break


def update_phonebook_item(item: Dict[str, str]) -> None:
    item_keys = list(item.keys())
    print('What to update: ')
    for ind, key in enumerate(item_keys):
        print('{}. {} ({})'.format(ind, key, item[key]))
    choice = int(input('Your choice: '))
    value = input('New value: ')
    item[item_keys[choice]] = value

def update_by_phone_number(phonebook: List[Dict[str, str]]) -> None:
    os.system('clear')
    result = None
    while True:
        required_name = input('Type phone number to search for: ')
        for item in phonebook:
            if item['phone'] == required_name:
                result = item
        if result is None:
            choice = input('Nothing, found, repeat? y/n ')
            if choice != 'y':
                break
            else:
                continue
        update_phonebook_item(result)
        break

def delete_by_phone_number(phonebook: List[Dict[str, str]]) -> None:
    os.system('clear')
    result = None
    while True:
        required_name = input('Type phone number to search for: ')
        for item in phonebook:
            if item['phone'] == required_name:
                result = item
        if result is None:
            choice = input('Nothing, found, repeat? y/n ')
            if choice != 'y':
                break
            else:
                continue
        result.clear()
        break


def system_exit(phonebook: List[Dict[str, str]]) -> None:
    json.dump(phonebook, open(file_name, 'w'))
    exit(0)

menu = {
    '1': ('Add new entries', add_new_entry),
    '2': ('Search by first name', search_by_first_name),
    '3': ('Search by last name', search_by_last_name),
    '4': ('Search by full name', search_by_full_name),
    '5': ('Search by city', search_by_city),
    '6': ('Search by phone number', search_by_phone),
    '7': ('Update a record for a given telephone number', update_by_phone_number),
    '8': ('Delete a record for a given telephone number', delete_by_phone_number),
    '9': ('Exit', system_exit)
}
while True:
    os.system('clear')
    print('Phonebook has {} entries'.format(len(phonebook)))
    for ind, name in menu.items():
        print('{}. {}'.format(ind, name[0]))
    choice = input('Make your choice: ')
    menu[choice][1](phonebook)
