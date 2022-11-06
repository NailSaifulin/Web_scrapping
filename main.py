import requests
from bs4 import BeautifulSoup
import fake_useragent
import re

HUBS = [
    "очередным"
    ]

ua =fake_useragent.UserAgent()
url = 'https://habr.com/ru/all/'
HEADERS = {
  "User-Agent": ua.chrome
}

response = requests.get(url, headers=HEADERS)
text = response.text
soup = BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    hubs = article.find_all("p")
    hubs = [hub.text.lower() for hub in hubs]
    hub = re.findall(r'\w+', str(hubs))
    for hb in HUBS:
       if hb.lower() in hub:
            href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
            full_href = f"https://habr.com{href}"
            title = article.find("h2").find("span").text
            datepost = article.find("time").attrs["title"]
            print(f"{datepost} ==> {title} ==> {full_href}")
            break