# Import selenium to access webpage
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriberWait

# WebScrap Library
from requests import get
from bs4 import BeautifulSoup

#def extract_indeed_jobs(keyword):

# Connection on url
base_url = "https://jp.indeed.com/jobs?q="
# Search items will be keyworld

keyword = "python"
response = get(f"{base_url}{keyword}")

if response.status_code != 200:
    print("Access denied", response.status_code)
else :
    # Set bs4 with html_doc, html.parse
    soup = BeautifulSoup(response.text, "html.parser")
    # Set result from response
    results = []

    #Get JobList
    job_list = soup.find("ul", class_="jobsearch-ResultList")
    jobs = job_list.find_all("li", recursive=False)
    print(len(jobs))