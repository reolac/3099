from bs4 import BeautifulSoup
from urllib.request import urlopen

from travel.getLogo import get_logo



urls = ['http://www.ukcinemas.org.uk/cinengland.html', 'http://www.ukcinemas.org.uk/cinother.html',
            'http://www.ukcinemas.org.uk/cinlondon.html']
result = []


for url in urls:
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html5lib')
    tables = soup.find_all("table", class_="Address")
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            link =  (row.find('a'))
            if link is not None and "http" in link.get('href'):
                ds = link.get('href')
                print (ds)
                print (get_logo(ds))
                #result.append((link.get('href')))

#print (result)


