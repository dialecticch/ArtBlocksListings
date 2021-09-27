from __future__ import print_function
import os.path
from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
import requests
import pandas as pd
import numpy as np

SPREADSHEET_ID = None
service = None
sheet = None


fidenza_rarity_sheet = pd.read_csv("Rarity_Sheets/fidenza_rarity_sheet.csv")
fidenza_rarity_array = np.array(fidenza_rarity_sheet[["rarity", "rank"]])
ringers_rarity_sheet = pd.read_csv("Rarity_Sheets/ringers_rarity_sheet.csv")
ringers_rarity_array = np.array(ringers_rarity_sheet[["rarity", "rank"]])
pigments_rarity_sheet = pd.read_csv("Rarity_Sheets/pigments_rarity_sheet.csv")
pigments_rarity_array = np.array(pigments_rarity_sheet[["rarity", "rank"]])
subscapes_rarity_sheet = pd.read_csv("Rarity_Sheets/subscapes_rarity_sheet.csv")
subscapes_rarity_array = np.array(subscapes_rarity_sheet[["rarity", "rank"]])
dino_rarity_sheet = pd.read_csv("Rarity_Sheets/dino_rarity_sheet.csv")
dino_rarity_array = np.array(dino_rarity_sheet[["rarity", "rank"]])
archetypes_rarity_sheet = pd.read_csv("Rarity_Sheets/archetypes_rarity_sheet.csv")
archetypes_rarity_array = np.array(archetypes_rarity_sheet[["rarity", "rank"]])
def fidenza_for_sale():
    url = "https://api.opensea.io/api/v1/assets"
    new_list = []
    for i in range(40):
        querystring = {"asset_contract_address": "0xa7d8d9ef8D8Ce8992Df33D8b8CF4Aebabd5bD270",
                       "token_ids": list(range(78000000+i*25, 78000000+(i+1)*25-1)),
                       "order_direction": "desc",
                       "offset": "0",
                       "limit": "50"}

        response = requests.request("GET", url, params=querystring)
        temp_list = list(response.json()['assets'])
        for j, el in enumerate(temp_list):
            if str(el['sell_orders']) != "None" and float(el['sell_orders'][0]['current_price']) / 1e18 < 500:
                id = int(el['token_id']) - 78000000
                last_price = "None"
                last_sale_date = "None"
                if str(el['last_sale']) != "None":
                    last_sale_date = el['last_sale']['event_timestamp']
                    last_price = float(el['last_sale']['total_price']) / 1e18
                current_price = float(el['sell_orders'][0]['current_price'])/ 1e18
                rarity = round(float(fidenza_rarity_array[id, 0]), 5)
                rank = str(int(fidenza_rarity_array[id, 1])) + "/1000"
                link = el["permalink"]
                created_date = el['sell_orders'][0]['created_date']
                timestamp = el['sell_orders'][0]['listing_time']
                new_list.append(["Art Blocks Fidenza",
                    id,
                    current_price,
                    rank,
                    created_date,
                    link,
                    rarity,
                    last_price,
                    last_sale_date,
                    timestamp])
    return new_list

def ringers_for_sale():
    url = "https://api.opensea.io/api/v1/assets"
    new_list = []
    for i in range(40):
        querystring = {"asset_contract_address": "0xa7d8d9ef8D8Ce8992Df33D8b8CF4Aebabd5bD270",
                       "token_ids": list(range(13000000+i*25, 13000000+(i+1)*25-1)),
                       "order_direction": "desc",
                       "offset": "0",
                       "limit": "50"}

        response = requests.request("GET", url, params=querystring)
        temp_list = list(response.json()['assets'])
        for j, el in enumerate(temp_list):
            if str(el['sell_orders']) != "None" and float(el['sell_orders'][0]['current_price']) / 1e18 < 500:
                id = int(el['token_id']) - 13000000
                last_price = "None"
                last_sale_date = "None"
                if str(el['last_sale']) != "None":
                    last_sale_date = el['last_sale']['event_timestamp']
                    last_price = float(el['last_sale']['total_price']) / 1e18
                current_price = float(el['sell_orders'][0]['current_price'])/ 1e18
                rarity = round(float(ringers_rarity_array[id, 0]), 5)
                rank = str(int(ringers_rarity_array[id, 1])) + "/1000"
                created_date = el['sell_orders'][0]['created_date']
                link = el["permalink"]
                timestamp = el['sell_orders'][0]['listing_time']
                new_list.append(["Art Blocks Ringers",
                    id,
                    current_price,
                    rank,
                    created_date,
                    link,
                    rarity,
                    last_price,
                    last_sale_date,
                    timestamp])
    return new_list

def pigments_for_sale():
    url = "https://api.opensea.io/api/v1/assets"
    new_list = []
    for i in range(41):
        querystring = {"asset_contract_address": "0xa7d8d9ef8D8Ce8992Df33D8b8CF4Aebabd5bD270",
                       "token_ids": list(range(129000000+i*25, 129000000+(i+1)*25-1)),
                       "order_direction": "desc",
                       "offset": "0",
                       "limit": "50"}

        response = requests.request("GET", url, params=querystring)
        temp_list = list(response.json()['assets'])
        for j, el in enumerate(temp_list):
            if str(el['sell_orders']) != "None" and float(el['sell_orders'][0]['current_price']) / 1e18 < 500:
                id = int(el['token_id']) - 129000000
                last_price = "None"
                last_sale_date = "None"
                if str(el['last_sale']) != "None":
                    last_sale_date = el['last_sale']['event_timestamp']
                    last_price = float(el['last_sale']['total_price']) / 1e18
                current_price = float(el['sell_orders'][0]['current_price'])/ 1e18
                rarity = round(float(pigments_rarity_array[id, 0]), 5)
                rank = str(int(pigments_rarity_array[id, 1])) + "/1024"
                link = el["permalink"]
                created_date = el['sell_orders'][0]['created_date']
                timestamp = el['sell_orders'][0]['listing_time']
                new_list.append(["Art Blocks Pigments",
                    id,
                    current_price,
                    rank,
                    created_date,
                    link,
                    rarity,
                    last_price,
                    last_sale_date,
                    timestamp])
    return new_list

def subscapes_for_sale():
    url = "https://api.opensea.io/api/v1/assets"
    new_list = []
    for i in range(32):
        querystring = {"asset_contract_address": "0xa7d8d9ef8D8Ce8992Df33D8b8CF4Aebabd5bD270",
                       "token_ids": list(range(53000000+i*25, 53000000+(i+1)*25-1)),
                       "order_direction": "desc",
                       "offset": "0",
                       "limit": "50"}

        response = requests.request("GET", url, params=querystring)
        temp_list = list(response.json()['assets'])
        for j, el in enumerate(temp_list):
            if str(el['sell_orders']) != "None" and float(el['sell_orders'][0]['current_price']) / 1e18 < 500:
                id = int(el['token_id']) - 53000000
                last_price = "None"
                last_sale_date = "None"
                if str(el['last_sale']) != "None":
                    last_sale_date = el['last_sale']['event_timestamp']
                    last_price = float(el['last_sale']['total_price']) / 1e18
                current_price = float(el['sell_orders'][0]['current_price'])/ 1e18
                created_date = el['sell_orders'][0]['created_date']
                rarity = round(float(subscapes_rarity_array[id, 0]), 5)
                rank = str(int(subscapes_rarity_array[id, 1]))+"/650"
                link = el["permalink"]
                timestamp = el['sell_orders'][0]['listing_time']
                new_list.append(["Art Blocks Subscapes",
                    id,
                    current_price,
                    rank,
                    created_date,
                    link,
                    rarity,
                    last_price,
                    last_sale_date,
                    timestamp])
    return new_list

def archetypes_for_sale():
    url = "https://api.opensea.io/api/v1/assets"
    new_list = []
    for i in range(30):
        querystring = {"asset_contract_address": "0xa7d8d9ef8D8Ce8992Df33D8b8CF4Aebabd5bD270",
                       "token_ids": list(range(23000000+i*25, 23000000+(i+1)*25-1)),
                       "order_direction": "desc",
                       "offset": "0",
                       "limit": "50"}

        response = requests.request("GET", url, params=querystring)
        temp_list = list(response.json()['assets'])
        for j, el in enumerate(temp_list):
            if str(el['sell_orders']) != "None" and float(el['sell_orders'][0]['current_price']) / 1e18 < 500:
                id = int(el['token_id']) - 23000000
                last_price = "None"
                last_sale_date = "None"
                if str(el['last_sale']) != "None":
                    last_sale_date = el['last_sale']['event_timestamp']
                    last_price = float(el['last_sale']['total_price']) / 1e18
                current_price = float(el['sell_orders'][0]['current_price'])/ 1e18
                created_date = el['sell_orders'][0]['created_date']
                rarity = round(float(archetypes_rarity_array[id, 0]), 5)
                rank = str(int(archetypes_rarity_array[id, 1]))+"/600"
                link = el["permalink"]
                timestamp = el['sell_orders'][0]['listing_time']
                new_list.append(["Art Blocks Archetypes",
                    id,
                    current_price,
                    rank,
                    created_date,
                    link,
                    rarity,
                    last_price,
                    last_sale_date,
                    timestamp])
    return new_list

def dinos_for_sale():
    url = "https://api.opensea.io/api/v1/assets"
    new_list = []
    for i in range(4):
        querystring = {"asset_contract_address": "0xa7d8d9ef8D8Ce8992Df33D8b8CF4Aebabd5bD270",
                       "token_ids": list(range(76000000 + i * 25, 76000000 + (i + 1) * 25 - 1)),
                       "order_direction": "desc",
                       "offset": "0",
                       "limit": "50"}

        response = requests.request("GET", url, params=querystring)
        temp_list = list(response.json()['assets'])
        for j, el in enumerate(temp_list):
            if str(el['sell_orders']) != "None" and float(el['sell_orders'][0]['current_price']) / 1e18 < 500:
                id = int(el['token_id']) - 76000000
                last_price = "None"
                last_sale_date = "None"
                if str(el['last_sale']) != "None":
                    last_sale_date = el['last_sale']['event_timestamp']
                    last_price = float(el['last_sale']['total_price']) / 1e18
                current_price = float(el['sell_orders'][0]['current_price']) / 1e18
                created_date = el['sell_orders'][0]['created_date']
                rarity = round(float(dino_rarity_array[id, 0]), 5)
                rank = str(int(dino_rarity_array[id, 1]))+"/100"
                link = el["permalink"]
                timestamp = el['sell_orders'][0]['listing_time']
                new_list.append(["Art Blocks Dino Pals",
                                 id,
                                 current_price,
                                 rank,
                                 created_date,
                                 link,
                                 rarity,
                                 last_price,
                                 last_sale_date,
                                 timestamp])
    return new_list

def update_sheet():
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'
        credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=scope)

        # If modifying these scopes, delete the file token.json.
        SPREADSHEET_ID = '1UXmle5eN7s7_FBz1NolTBtLL5u2clYnCXt1OM2j5jdE'

        service = build('sheets', 'v4', credentials=credentials)

        fidenza_list = fidenza_for_sale()
        ringers_list = ringers_for_sale()
        pigments_list = pigments_for_sale()

        archetypes_list = archetypes_for_sale()
        dino_list = dinos_for_sale()
        subscapes_list = subscapes_for_sale()


        final_list = fidenza_list + ringers_list + pigments_list + dino_list + archetypes_list + subscapes_list
        final_list.sort(key=lambda x: x[9], reverse=True)
        final_list.insert(0, ["Collection","Id", "Current Price", "Rarity Rank", "Listing Date", "Link", "Rarity", "Last Price", "Last Sale Time", "Timestamp"])
        body = {}
        service.spreadsheets().values().clear(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A:Z",
                                              body=body).execute()
        resource = {
            "majorDimension": "ROWS",
            "values": final_list
        }
        range = "Sheet1!A:A"
        service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=range,
            body=resource,
            valueInputOption="USER_ENTERED"
        ).execute()


update_sheet()
