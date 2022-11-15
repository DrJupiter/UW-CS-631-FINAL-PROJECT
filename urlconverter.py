import urllib.parse
import requests

s, e = "http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/", "-TAVG-Trend.txt"

with open("country-list.txt", 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        url = s + urllib.parse.quote(line.strip().lower().replace(" ", "-").encode('cp1252')) + e
        response = requests.get(url)
        with open(f"./files/{line.strip().lower()}.txt", 'wb') as f:
            f.write(response.text.encode('utf-8'))
            f.close()
        

