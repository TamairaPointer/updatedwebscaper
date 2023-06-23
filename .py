import requests
from bs4 import BeautifulSoup

# The URL of the webpage you want to scrape
url = 'https://www.indeed.com/...'

# Keywords or phrases you are interested in
keywords = ['Dental', 'Software Engineer', 'Data Scientist']

# Send a HTTP request to the URL
response = requests.get(url)

# If request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the h2 tags with class "jobTitle css-1h4a4n5 eu4oa1w0"
    job_title_tags = soup.find_all('h2', {'class': 'jobTitle css-1h4a4n5 eu4oa1w0'})
    
    # Loop through each job title tag found
    for job_title_tag in job_title_tags:
        # Find the nested anchor tag within the h2 tag
        anchor_tag = job_title_tag.find('a', {'class': 'jcs-JobTitle css-jspxzf eu4oa1w0'})
        
        # If the anchor tag is found
        if anchor_tag:
            # Extract the title from the span tag inside the anchor tag
            title_tag = anchor_tag.find('span', {'id': lambda x: x and x.startswith('jobTitle-')})
            
            # If the title tag is found
            if title_tag:
                # Extract the job title text
                job_title_text = title_tag.get("title")
                
                # Check if the job title contains any of the keywords
                if any(keyword in job_title_text for keyword in keywords):
                    # Print the job title
                    print(f'Job Title: {job_title_text}')
else:
    print('Failed to retrieve the webpage')
