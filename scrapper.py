from bs4 import BeautifulSoup
import requests

url = "https://www.naukri.com/job-listings-data-scientist-business-analyst-science-data-analyst-megara-infotech-bhubaneswar-mumbai-hyderabad-secunderabad-gurgaon-gurugram-bangalore-bengaluru-delhi-ncr-0-to-1-years-310323003909?src=discovery_trendingWdgt_homepage_srch&sid=16802765936445865&xp=1&px=1"
response = requests.get(url).text
result = BeautifulSoup(response, 'html.parser')
print(result.prettify())