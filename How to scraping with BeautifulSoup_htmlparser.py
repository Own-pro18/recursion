from bs4 import BeautifulSoup
import requests


def scrap():
    page = requests.get('https://www.example.co.uk')
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    return (soup.find_all('a'))
print(scrap())
