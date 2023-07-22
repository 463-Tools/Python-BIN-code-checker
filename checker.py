# Path: checker.py
from requests import get
from prettytable import PrettyTable
api = "https://lookup.binlist.net/"

def check_bin(bins):
    p =b= None
    # Create new table
    table = PrettyTable()
    table.field_names = ['CARD NUM','CARD SCHEME', 'CARD TYPE', 'CARD BRAND', 'CARD PREPAID', 'CARD COUNTRY', 'CARD BANK']

    # Query data
    for x in bins:
        try:
            query = get(f"{api}{x}",
                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 
                "Accept-Version": "3"}).json()
        except Exception as e:
            print(e)
            pass
        print(f'Quering {x}')
        #print(query)
        
        # Sort data
        try: 
            if query["prepaid"]: p = query["prepaid"]
            if query["bank"]: b = f'{query["bank"]["name"]}({query["bank"]["url"]})'
            table.add_row([x, query["scheme"], query["type"], query["brand"], p, f'{query["country"]["name"]}({query["country"]["emoji"]} )', b])
        except: pass
    
    # Export data
    print(table)