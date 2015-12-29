from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_logo(url):
    try:
        logo = ""
        if "pontio" not in (url):
            html = urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')
            data = (soup.find_all(["img"],src=True))

            for line in data:
                if ("logo" in line["src"]):
                    logo = (line["src"])
                    break

            if not logo and data:
                logo = data[0].get('src')
            if ("http" not in logo):
                logo = url + '/' + logo

            return (logo)
        else:
            return (logo)
    except:
        print ("")






