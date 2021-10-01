from bs4 import BeautifulSoup
import requests


def scrap():
    page = requests.get('https://www.ox.ac.uk/admissions')
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    return (soup.find_all('a'))

print(scrap())