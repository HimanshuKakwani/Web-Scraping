from bs4 import BeautifulSoup
import requests

html_texts = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_texts)
soup = BeautifulSoup(html_texts, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
for job in jobs:

    time_posted = job.find('span', 'sim-posted').span.text
    if 'few' in time_posted:
        comp = job.find('h3', class_ = 'joblist-comp-name').text
        skills = job.find('span', class_ = 'srp-skills').text
# print(comp.text.replace(' ', ''))
# print(skills.text)

        print(f'''
        Company Name: {comp}
        Req skills: {skills}
        ''')