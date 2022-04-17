from parameters import *
from utils import *
import time

print('[start] Extract data from website')
projects = []
for url in URLS_TO_SCRAP:
    projects += get_projects_from(url)
    time.sleep(1)

projects = sorted(
    projects, key=lambda project: project['launched_at'], reverse=True)
try:
    create_output_directory()
    filename = generate_file_from(CSV_HEADER, projects)

    print('[end] Done! Csv file generated, please check {}'.format(
        os.getcwd() + '/' + CSV_OUTPUT_FILEPATH + filename))

    print('[end] For support projects 👉 {}'.format(FUNDRAISER_URL))
except Exception as err:
    print('😲 An error occurred:', err)
