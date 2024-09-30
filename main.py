import requests
from bs4 import BeautifulSoup

raw = requests.get('https://hkust.edu.hk/stu_intranet/')
text = BeautifulSoup(raw.text, 'html.parser')
print(text.prettify())
