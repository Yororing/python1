#pip library
from requests import get
from bs4 import BeautifulSoup

#import component from other files
from extractors.wwr import extract_wwr_jobs
#from extractors.indeed import extract_indeed_jobs

java_jobs = extract_wwr_jobs("java")
print(java_jobs)

#python_jobs = extract_indeed_jobs("python")
#print(python_jobs)


