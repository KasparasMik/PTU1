from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.scrapethissite.com/pages/simple/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'html.parser')
blokas = soup.find('div', class_="row")


h3tags = soup.find_all('h3')
div = soup.find_all('div', class_="col-md-4 country")

tags = soup.find_all(['span', 'strong'])



for soups in div:
    print(soups.text.strip())
    for soup in soups:
        print(soup.text.strip())


