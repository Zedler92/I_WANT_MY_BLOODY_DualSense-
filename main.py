import datetime
from bs4 import BeautifulSoup
import requests
from email_manager import send_email
BLOODY_PAD = "https://www.amazon.pl/Sony-DualSense-Kontroler-Bezprzewodowy-Cosmic/dp/B094WRT8PD/ref=sr_1_12?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2YP8E01NIQSJO&keywords=ps5+pad&qid=1661150572&sprefix=ps5+pad%2Caps%2C85&sr=8-12"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
response = requests.get(url=BLOODY_PAD, headers=headers)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
price = soup.find(name="span", class_="a-price-whole")
price = int(price.getText().strip(","))

if price < 360:
    send_email(price, BLOODY_PAD)



