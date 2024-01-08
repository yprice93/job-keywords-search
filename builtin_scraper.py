import requests
from bs4 import BeautifulSoup

BUILTIN_URL = "https://builtin.com/jobs?search="
BIJD_URL = "https://builtin.com"

# def extract_id(pattern, input_string):
#     match = re.search(pattern, input_string)
#     if match:
#     # Access the captured group to get the value
#         job_id_value = match.group(1)
#         return job_id_value
#     else:
#         print("No match found.")
        

job_hrefs = []
tech_stack = ["java", "spring", "mySQL", "ruby on rails", "postgres", "django", "go", "node", "kotlin", "rust", "php", "javascript", "vue", "next"]
matching_paragraphs_collection = []


for webPage in range(1,100):
    page = requests.get(BUILTIN_URL + "full+stack&page=" + str(webPage))


    soup = BeautifulSoup(page.content, 'html.parser')
    # Find all li tag
    main_elements = soup.find_all(id="job-card-alias")
    
    for el in main_elements:
        url = el.get('href')
        job_hrefs.append(url)
        


for href in job_hrefs:
    page = requests.get(BIJD_URL + href)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find all paragraphs (p elements) on the page
    paragraphs = soup.find_all('p')

    # Filter and save paragraphs containing specified keywords
    matching_paragraphs = [p.text.strip() for p in paragraphs if any(keyword.lower() in p.text.lower() for keyword in tech_stack)]
    matching_paragraphs_collection.append(matching_paragraphs)
    

    # Print or save the matching paragraphs
  
    for i, paragraph in enumerate(matching_paragraphs_collection, 1):
        print(f"Matching Paragraph {i}:\n{paragraph}\n")
    
    # Optionally, you can save the matching paragraphs to a file
        with open('matching_paragraphs.txt', 'w', encoding='utf-8') as file:
            file.write('\n\n'.join(matching_paragraphs))

        

    
    

    



