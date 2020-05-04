import csv

def get_users():
    """READ FROM "USERS.CVS" FILE"""
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        users = [i for i in reader]
    return users

def get_goods():
    """READ FROM 'GOODS.CVS' FILE"""
    with open('goods.csv', 'r') as file:
        reader = csv.DictReader(file)
        goods = [i for i in reader]
    return goods

def get_stores():
    """READ FROM 'STORES.CVS' FILE"""
    with open('stores.csv', 'r') as file:
        reader = csv.DictReader(file)
        stores = [i for i in reader]
    return stores

