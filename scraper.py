from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
# from fake_useragent import UserAgent

# ua = UserAgent()
# userAgent = ua.random
url = "https://www.naukri.com/job-listings-data-scientist-business-analyst-science-data-analyst-megara-infotech-bhubaneswar-mumbai-hyderabad-secunderabad-gurgaon-gurugram-bangalore-bengaluru-delhi-ncr-0-to-1-years-310323003909?src=discovery_trendingWdgt_homepage_srch&sid=16802765936445865&xp=1&px=1"
url1 = "https://www.amazon.com/HyperX-Cloud-Gaming-Headset-KHX-HSCP-RD/dp/B00SAYCXWG/ref=sr_1_3?keywords=gaming+headsets&pd_rd_r=81d651ab-6c1a-430d-916d-9808d6e835ca&pd_rd_w=nWRzy&pd_rd_wg=8N6in&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=KSAAT5QMHQXPM2K6HEY3&qid=1680429941&sr=8-3"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--verbose")
chrome_options.add_argument("--window-size=1920, 1200")
# chrome_options.add_argument('--headless')

chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
doc = BeautifulSoup(driver.page_source, "html.parser")
# print(doc)

title = ' '.join(doc.find('h1', attrs={'class': 'jd-header-title'}).text.split())
company = doc.find('div', attrs={'class': 'jd-header-comp-name'}).find('a').text
location_tag = doc.find('div', attrs={'class': 'loc'}).find_all('a')
locations = []
for loc in location_tag:
    locations.append(loc.text.strip())
location = ', '.join(locations)
salary_container = doc.find('div', attrs={'class': 'exp-salary-container'})
exp_tag = salary_container.find('div', attrs={'class': 'exp'})
experience_required = exp_tag.find('span').text.strip()
salary_tag = salary_container.find('div', attrs={"class": 'salary'})
salary_range = salary_tag.find('span').text.strip()
skills_tags = doc.find('div', attrs={'class': 'key-skill'}).find_all('a', attrs={'class':'chip clickable'})
skills = []
for skill in skills_tags:
    skills.append(skill.find('span').text)
skills_required = ', '.join(skills)
job_description = doc.find('div', attrs={'class':'dang-inner-html'}).text
date_of_posting = doc.find('div', attrs={'class': "jd-stats"}).find('span', attrs={'class': 'stat'}).find('span').text.strip()

job_details = doc.find_all('div', attrs={'class':'details'})
job_type_temp = [job_detail for job_detail in job_details if job_detail.text.find('Employment Type') != -1]
job_type = job_type_temp[0].find('span').text.strip()

job_data = {}
job_data['Job_title'] = title
job_data['Company_name'] = company
job_data['Location'] = location
job_data['Experience_required'] = experience_required
job_data['Skills_required'] = skills_required
job_data['Job_description'] = job_description
job_data['Salary_range'] = salary_range
job_data['Date_of_posting'] = date_of_posting
job_data['Job_type'] = job_type

print(json.dumps(job_data))
