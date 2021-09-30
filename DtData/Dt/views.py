from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup


def index(request):
    return HttpResponse("I Love My New Page")


def main(request):
    return HttpResponse("I Love My Old website")


def req(request):
    page = requests.get(
        'https://www.uxbridgecollege.ac.uk/courses-west-london/gcse/76-level-2-13/6451-functional-skills-english-pre-gcse-level-2-pt-evening.html')
    return HttpResponse(page.content)


def oxford(request):
    page = requests.get('https://www.ox.ac.uk/admissions')
    return HttpResponse(page.content)


def scrap(request):
    page = requests.get('https://www.ox.ac.uk/admissions')
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    return HttpResponse(soup.find_all('a'))

# Create your views here.
