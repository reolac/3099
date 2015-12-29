from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_cinema_locations():
    urls = ['http://www.ukcinemas.org.uk/cinengland.html', 'http://www.ukcinemas.org.uk/cinother.html',
        'http://www.ukcinemas.org.uk/cinlondon.html']
    result = []

    for url in urls:
        print (url)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html5lib')
        result.extend(soup.find_all("span", class_="Townheader"))

    return (result)