import requests
from time import sleep
from bs4 import BeautifulSoup

class flicpic(object):
    url = "https://api.flickr.com/services/feeds/photos_public.gne?format=json"
    response = requests.get(url)
    page = str(BeautifulSoup(response.content))
    def getlink(self,page):
        start = page.find("src")
        if start == -1:
            print None
        begin = page.find('"',start)
        end = page.find('\\',begin+1)
        link = page[begin + 1: end]
        return link,end

    def getall(self):
        while True:
            link, n = self.getlink(flicpic.page)
            flicpic.page = flicpic.page[n:]
            if link:
                print link
            else:
                break
if __name__ == '__main__':
    fr = flicpic()
    fr.getall()
