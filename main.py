from turtle import title
from requests import get
from bs4 import BeautifulSoup

# Connection on url
base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="

# Search items
search_term = "python"

# Set response
response = get(f"{base_url}{search_term}")

# Function which is get data from base_url
def getData():
    # Set bs4 with html_doc, html.parse
    soup = BeautifulSoup(response.text, "html.parser")

    # Set result from response
    results = []

    # This get All by searching tag & class
    # Examples
    # print(soup.find_all('title'))
    # print(soup.find_all('section', class_="jobs"))
    jobs = soup.find_all('section', class_="jobs")

    for job_section in jobs:
        job_posts = job_section.find_all('li')
        # Remove li = view all
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']

            # Get company, kind, region
            company, kind, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_="title")

            job_data = {
                'link' : f"https://weworkremotely.com{link}",
                'company': company.string,
                'kind' : kind.string,
                'region': region.string,
                'position': title.string,
            }
            results.append(job_data)

    return results

# If the connection to this url is not possible then send log
if response.status_code != 200:
    print("Can't request website")
# Else get this url's html and send log
else:
    print("Access Succesfully")
    print(getData())






