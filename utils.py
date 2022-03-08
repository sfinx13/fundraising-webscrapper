import cloudscraper
import csv
import math
import os
import time
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from parameters import *

def get_emoji_by(percentage_raised):
    if percentage_raised == "-":
        return "🤷 "
    elif percentage_raised >= 100:
        return "🌞 "
    elif percentage_raised > 79:
        return "☀️ "
    elif percentage_raised > 49:
        return "🌤️ "
    elif percentage_raised > 19:
        return "🌥️ "
    else:
        return "☁️ "

def format_date(date_string):
    if ("Launched the" in date_string):
        return datetime.strptime(date_string[13:], '%d %b %Y').strftime("%Y-%m-%d")
    else:
        day_elapsed = [int(i) for i in date_string.split() if i.isdigit()]
        return (date.today() - timedelta(day_elapsed.pop())).strftime("%Y-%m-%d")

def generate_file_from(fieldnames, projects):
    filename = "projects-" + time.strftime("%Y%m%d-%H%M%S") + '.csv'
    with open(CSV_OUTPUT_FILEPATH + filename, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for project in projects:
            writer.writerow(project)
    
    return filename

def create_output_directory():
    try:
        os.mkdir(CSV_OUTPUT_FILEPATH)
    except OSError:
        pass

def get_projects_from(url):
    scrapper = cloudscraper.create_scraper()
    soup = BeautifulSoup(scrapper.get(url).text, 'html.parser')

    projects = []
    wrappers = soup.find_all("div", class_="thumbnail-wrapper")

    for project in wrappers:
        try:
            nb_people_or_amount_total = project.select_one(
                '.price-total span').string
            nb_people = int(
                nb_people_or_amount_total) if "€" not in nb_people_or_amount_total else "-"
            amount_total = nb_people_or_amount_total.replace(
                " ", "")[:-1] if "€" in nb_people_or_amount_total else "-"
            amount_raised = int(project.p.string.replace(" ", "")[:-1])
            percentage_raised = math.ceil(
                amount_raised / int(amount_total) * 100) if "-" != amount_total else "-"
            launched_at = project.select_one(
                '.organize-by-all').text.split('\n\n')[1].replace('\n', '')

            projects.append({
                "title": project.h2.string,
                "fundraiser": project.select_one('.organize-by-all span').string,
                "amount_raised": amount_raised,
                "nb_people": nb_people,
                "amount_total":  amount_total,
                "percentage_raised": str(percentage_raised) + " %" if "-" != percentage_raised else "-",
                "average_raised": amount_raised // nb_people if "-" != nb_people else "-",
                "launched_at": format_date(launched_at)
            })

            print("✅ {} {} - 💰 {} € raised".format(get_emoji_by(percentage_raised),
                  project.h2.string, amount_raised))
        except (AttributeError, ValueError):
            print("❌ {}".format(project.h2.string))

    return projects
