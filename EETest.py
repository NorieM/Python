from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import re

content = requests.get("https://www.adelaideairport.com.au/flight-information/flight-search/?flt_no=&carrier=All&city=&dte=Tomorrow&leg=")

soup = BeautifulSoup(content.text, "lxml")

flights = soup.find_all('div', class_='SearchResultFlightListRow')

for flight in flights:    

    airline = flight.find('div', {'class': re.compile('flightNumberLogo')}).find_all('img')[0]['alt']

    flightno =flight.find('div', {'class': re.compile('flightNumberLogo')}).find_all('p')[1].text

    origin = flight.find('div', {'class': re.compile('col-dest')}).find_all('p')[0].text
    dest = flight.find('div', {'class': re.compile('col-dest')}).find_all('p')[1].text

    scheduled = flight.find('div', {'class': re.compile('col-sched')}).find_all('p')[0].text
    estimated = flight.find('div', {'class': re.compile('col-sched')}).find_all('p')[1].text

    print(f'Airline:{airline} Flight No:{flightno} Origin:{origin} Destination:{dest}')