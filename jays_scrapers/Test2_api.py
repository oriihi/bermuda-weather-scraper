import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/jriihi/opt/anaconda3/lib/python3.7/Test_API/creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("Bermuda_weather_data").sheet1

data = sheet.get_all_records()

pprint (data)

test_add = ['Back','it up again','Terry']

sheet.append_row(test_add)
