# Path: checker.py
import json
import requests
import os
from datetime import date
from prettytable import PrettyTable
import csv

#api = "https://lookup.binlist.net/"
#api = "https://api.freebinchecker.com/bin/"
with open('config.json', 'r') as f:
    config = json.load(f)
    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': config["API"]["key"],
        'X-RapidAPI-Host': config["API"]["host"]
    }

def check_bin(bins):
    # Create new table
    table = PrettyTable()
    table.field_names = ['CARD NUM', 'VALID', 'CURENCY', 'CARD SCHEME', 'CARD TYPE', 'CARD BRAND', 'CARD COUNTRY']

    # Create new csv file
    d = date.today().strftime('%m_%d_%Y')
    i = 1
    filename = f'result-{d}.csv'
    while os.path.exists(filename):
        base, ext = os.path.splitext(filename)
        filename = f"{base}_{i}{ext}"
        i += 1
    export = open(filename, 'a+', newline='')
    writer = csv.writer(export)
    writer.writerow(['CARD NUM', 'VALID', 'CURENCY', 'CARD SCHEME', 'CARD TYPE', 'CARD BRAND', 'CARD COUNTRY', 'LEVEL', 'ISSUER', 'REGION', 'SUBREGION', 'CAPITAL', 'NUMERIC'])

    # Query data
    for x in bins:
        try:
            querystring = {"bin": x}
            payload = { "bin": x }
            response = requests.post('https://'+config["API"]["host"], json=payload, headers=headers, params=querystring)
            print(response)
            query = response.json()
        except Exception as e:
            print(e)
            pass
        print(f'Quering {x}...')
        
        # Sort data
        try:
            print('Success.' if query['success'] else 'Failed')
        except:
            print('Failed')
            pass
        try:
            card = query['BIN']
            row1 = [card['number'], card['valid'], card['currency'], card["scheme"], card["type"], card["brand"], card["country"]["name"]]
            row2 = [card['number'], card['valid'], card['currency'], card["scheme"], card["type"], card["brand"], card["country"]["name"], card['level'], f"{card['issuer']['name']} ({card['issuer']['website']})", card['country']['region'], card['country']['subregion'], card['country']['capital'], card['country']['numeric']]
            table.add_row(row1)
            writer.writerow(row2)
        except: pass
    
    # Export data
    print(table)