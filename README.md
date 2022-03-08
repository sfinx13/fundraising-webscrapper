# Web scrapping from fundraising platform

![This is an image](/_DOC/app_screen.png)

## Installation
```bash
docker build -t app-webscrapping .
docker run -it -v "$PWD":/app app-webscrapping
```

CSV exports are generated at `output` directory

## Links
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* https://github.com/venomous/cloudscraper