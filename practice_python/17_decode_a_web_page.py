'''
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the New York Times homepage.
'''
from bs4 import BeautifulSoup
import requests


url = 'http://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text)

for heading in soup.find_all(class_='story-heading'):
    if heading.a:
        print(heading.a.text.replace("\n", " ").strip())
    else:
        print(heading.contents[0].strip())
