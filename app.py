from parameters import *
from utils import *

print('[start] Scrape data from cotizup website')
projects = []
for url in URLS_TO_SCRAP:
    projects += get_projects_from(url)

projects = sorted(
    projects, key=lambda project: project['launched_at'], reverse=True)


filename = generate_file_from(CSV_HEADER, projects)

print('[end] Done! Csv file generated, please check {}'.format(
    os.getcwd() + '/' +  CSV_OUTPUT_FILEPATH + filename))

print('[end] For support projects 👉 {}'.format(FUNDRAISER_URL))
