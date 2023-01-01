#import component from other files
#from extractors.wwr import extract_wwr_jobs
#from extractors.indeed import extract_indeed_jobs
#from extractors.file import save_to_file

#import Flask
from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html")

app.run("127.0.0.1:6000")

#keyword = input("What do you want to search for? :")
#
#indeed = extract_indeed_jobs(keyword)
#weWorkRemote = extract_wwr_jobs(keyword)
#
#jobs = indeed + weWorkRemote
#
#save_to_file(keyword, jobs)



