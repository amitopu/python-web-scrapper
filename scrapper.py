from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/creality-ender-3-v2-white/p/288-00B4-000E8?quicklink=true"
response = requests.get(url).text
result = BeautifulSoup(response, 'html.parser')
print(result.prettify())