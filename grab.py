import csv
import sys
import requests
import os

def setupdir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        return True
    return False

def get_photo(id, url, dirname):
    print url

    if not url: return

    chunk_size = 1024
    if not os.path.exists("photos"):
        os.mkdir("photos")
    dirname = os.path.join("photos", dirname)
    setupdir(dirname)

    filename = os.path.join(dirname, id)
    r = requests.get(url, stream=True)
    if not os.path.exists(filename):
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)

filename = sys.argv[1]

reader = csv.reader(open(filename))
headers = reader.next()

for row in reader:
    datum = dict(zip(headers, row))
    get_photo(datum["ID"], datum["signature"], "signature")
    get_photo(datum["ID"], datum["signature_interviewee"], "signature_interviewee")
    get_photo(datum["ID"], datum["ecd_centre_photo"], "centre_photo")
    get_photo(datum["ID"], datum["structured_learning_daily_programme_photo"], "daily_programme")
    get_photo(datum["ID"], datum["grade_r_structured_learning_daily_programme_photo"], "grade_r_structured_learning_daily_programme_photo")
    get_photo(datum["ID"], datum["site_outside_dangerous_obstacles_photo"], "dangerous_obstacles")
    get_photo(datum["ID"], datum["daily_menu_photo"], "daily_menu_photo")
    get_photo(datum["ID"], datum["roof_condition_visible_defects_photo"], "roof")
    get_photo(datum["ID"], datum["inside_condition_cracks_leaks_photo"], "cracks")
    get_photo(datum["ID"], datum["plumbing_condition_visible_leaks_photo"], "plumbing")

