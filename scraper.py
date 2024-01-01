import requests
from bs4 import BeautifulSoup
import re

BUILTIN_URL = "https://builtin.com/jobs?search="
page = requests.get(BUILTIN_URL + "full+stack")


soup = BeautifulSoup(page.content, 'html.parser')
# Find all li tag
main_elements = soup.find_all(class_="font-barlow fs-md fs-xl-xl d-inline-block m-0 hover-underline")
# href_elements = soup.find_all('a', href=True)

# for el in href_elements:
#     print(el)



# Define a regular expression pattern to extract the value of data-builtin-track-job-id
pattern = r'data-builtin-track-job-id="(\d+)"'

# Use the re.search() function to find the match


# Check if a match is found
def extract_id(pattern, input_string):
    match = re.search(pattern, input_string)
    if match:
    # Access the captured group to get the value
        job_id_value = match.group(1)
        return job_id_value
    else:
        print("No match found.")
        
job_ids = []

for el in main_elements:
    el_string = str(el)
    id = extract_id(pattern, el_string)
    job_ids.append(id)

for id in job_ids:
    print(id)
    
    
    