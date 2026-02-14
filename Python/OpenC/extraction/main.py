import requests
from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

title = soup.title
id = soup.find(id='titre')
print(title, id)