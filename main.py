#import component from other files
from ast import keyword
from curses import keyname
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.file import save_to_file

#import Flask
from flask import Flask, render_template, request, redirect, send_file

app = Flask("JobScrapper")

#Save the results of search
data_dictionary = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    #Prevent None search request
    if keyword == None :
        return redirect("/")

    if keyword in data_dictionary:
        jobs = data_dictionary[keyword]
    else :
        indeed = extract_indeed_jobs(keyword)
        weWorkRemote = extract_wwr_jobs(keyword)
        jobs = indeed + weWorkRemote
        data_dictionary[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)

#CSV export
@app.route("/export")
def export():
    keyword = request.args.get("keyword")

    #Prevent None keyword
    if keyword == None :
        return redirect("/")

    #Prevent if doesnt search anything but get CSV data file
    if keyword not in data_dictionary:
        return redirect(f"/search?keyword={keyword}")

    save_to_file(keyword, data_dictionary[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("127.0.0.1", port=5500, debug=True)




