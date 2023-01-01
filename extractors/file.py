def save_to_file(file_name, jobs):
    #Make csv file
    file = open(f"{file_name}.csv", "w", encoding="utf-8")
    file.write("Position, Company, Location, URL, Kind\n")

    for job in jobs:
        file.write(f"{job['position']}, {job['company']}, {job['region']}, {job['link']}, {job['kind']}\n")

    file.close()
