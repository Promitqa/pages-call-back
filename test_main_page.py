import csv
from main_page import MainPage


def read_links():
    links = []
    with open('/Users/alexwell/Downloads/links.csv') as csvfile:
        linksReader = csv.reader(csvfile, delimiter=',')
        for row in linksReader:
            links.append(row[0])
        return links


def test_find_button(browser):
    links = read_links()
    for link in links:
        browser.get(link)
        page = MainPage(browser, link)
        page.open()
        page.find_element_button()
