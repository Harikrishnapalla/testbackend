import requests

url = "https://world-population.p.rapidapi.com/population"

querystring = {"country_name":"Mexico"}

headers = {
    'x-rapidapi-host': "world-population.p.rapidapi.com",
    'x-rapidapi-key': "d8daa63eedmsh7c79431f2cc27cbp19b4bajsne42ce35b38c4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)