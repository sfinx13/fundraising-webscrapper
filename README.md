# Web scrapping from fundraising platform

![Screenshoot website](/_DOC/website_screen.png)

![Screenshoot console application](/_DOC/app_screen.png)

## Installation
```bash
docker build -t app-webscrapping .
docker run -it -v "$PWD":/app app-webscrapping
```

## Output

> Console displays project list with emoji for tracking

### Emoji meaning

|Emoji|Description  | Percentage raised
|--|--|--|
|🤷| Not enough data  |  - 
|🌞| Successul project | 100%|
|☀️| On very good track| > 79%
|🌤️| Nice work, a little effort |> 49%
|🌥️ | Share the project around you | > 20%
|☁️ | Thank you for you support   | < 20%


> CSV exports are generated at `output` directory, files are timestamped

![Screenshoot output csv folder](/_DOC/csv_folder_screen.png)

![Screenshoot content csv](/_DOC/csv_screen.png)

## Links
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* https://github.com/venomous/cloudscraper