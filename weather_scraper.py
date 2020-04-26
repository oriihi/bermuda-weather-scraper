 #!/Users/oliverriihiluoma/Documents/personal/projects/weather_scraper/env/bin/python

import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime


URL = 'http://weather.bm/'
page = requests.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')
job_elems = soup.find_all('div', class_='obElementRight')



windSpeed = ""
windDirectionStr = job_elems[2].text.split()[0]


for char in job_elems[2].text.split()[1]:
    if char.isnumeric():
        windSpeed += char 

if windDirectionStr == "N":
    windDirectionNum = 0
elif windDirectionStr =="NNE":
    windDirectionNum = 22.5
elif windDirectionStr =="NE":
    windDirectionNum = 45
elif windDirectionStr =="ENE":
    windDirectionNum = 67.5
elif windDirectionStr =="E":
    windDirectionNum = 90
elif windDirectionStr =="ESE":
    windDirectionNum = 112.5
elif windDirectionStr =="SE":
    windDirectionNum = 135
elif windDirectionStr =="SSE":
    windDirectionNum = 157.5
elif windDirectionStr =="S":
    windDirectionNum = 180
elif windDirectionStr =="SSW":
    windDirectionNum = 202.5
elif windDirectionStr =="SW":
    windDirectionNum = 225
elif windDirectionStr =="WSW":
    windDirectionNum = 247.5
elif windDirectionStr =="W":
    windDirectionNum = 270
elif windDirectionStr =="WNW":
    windDirectionNum = 292.5
elif windDirectionStr =="NW":
    windDirectionNum = 315
elif windDirectionStr =="NNW":
    windDirectionNum = 327.5

print(windDirectionNum)
print(windSpeed)

humidity = job_elems[1].text[0:2]  
tempC = job_elems[0].text[0:2]
dateTimeObj = datetime.now()
print(dateTimeObj)
with open('data.csv', 'a', newline='') as file:  #the 'a' says to append where as a 'w' would write (from scratch)
    writer = csv.writer(file)
    writer.writerow([dateTimeObj, tempC, humidity, windDirectionNum, windSpeed])
    print("writing")


