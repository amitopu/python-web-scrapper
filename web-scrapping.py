from bs4 import BeautifulSoup
import json

with open('page.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

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