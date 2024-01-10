import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?"
job_ids = []

# for webPage in range(1,3000):
page = requests.get(LINKEDIN_URL + "keywords=backed%20engineer" )


soup = BeautifulSoup(page.content, 'html.parser')
    # Find all li tag
divs_with_data_job_id = soup.find_all('div', {'data-job-id': True})

for div in divs_with_data_job_id:
    print(div)
    # Access attributes or text content as needed
    # job_id = div['data-job-id']
    # Do something with the job_id

  
