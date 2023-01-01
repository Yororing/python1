# Import selenium to access webpage
import selenium
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

# WebScrap Library
from requests import get
from bs4 import BeautifulSoup


#Set Options
options = Options()
options.add_argument("--no--sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

# Set url to indeed.com
base_url = "https://jp.indeed.com/jobs"

def get_page_count(keyword):
    # Connection on url
    browser.get(f"{base_url}?q={keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="css-jbuxu0 ecydgvn0")

    #if 1page only then return it has one page only
    if pagination == None:
        return 1

    #else get pages max 5pages
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else :
        return count

def extract_indeed_jobs(keyword):
    print("Access Succesfully")
    # get pages from get_page_count
    pages = get_page_count(keyword)
    print("Found", pages, "pages (Max 5pages)")
    for page in range(pages):
        # Connection on url
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        browser.get(final_url)
        print("Requesting", final_url)

        # Set result for return
        results = []
        soup = BeautifulSoup(browser.page_source, "html.parser")

        job_list = soup.find("ul", class_ = "jobsearch-ResultsList")

        jobs = job_list.find_all("li", recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                # Find <a> to find job title and link
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_= "companyName")
                location = job.find("div", class_= "companyLocation")
                kind_list = job.find("ul", class_="JobTags-list")
                kind = job.find("li")

                # Set result
                job_data = {
                'link' : f"https://jp.indeed.com{link}",
                'company': company.string,
                'kind' : '',
                'region': location.string,
                'position': title,
                }

                for each in job_data:
                    if job_data[each] != None:
                        job_data[each] = job_data[each].replace(",", " ")

                results.append(job_data)
    return results
