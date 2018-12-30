import bs4 as  bs
import urllib.request
from googlesearch import search
import sys
import re
import lxml


class LIST():


    def find_tracklist(self,album_name,artist):
        search_string = "Wikipedia Album "+album_name+" "+artist
        for i in search(search_string,tld="com",lang="em",num=1,start=0,stop=1,pause = 2.0):
            return str(i)

    def __init__(self,album_name,artist):
        self.l = []
        link = self.find_tracklist(album_name,artist)
        r = urllib.request.urlopen(link).read()
        soup =  bs.BeautifulSoup(r,'lxml')
        body = soup.body

        for table in body.find_all('table',{'class':['tracklist']} ):
            for td in table.find_all('td',{'style' : ['vertical-align:top']}):
                if td.text[0].isalpha()==False:
                    self.l.append(td.text.replace('"'," "))

    def throwlist(self):

        return self.l
if __name__ == "__main__":
    a = LIST("kids see ghosts","kanye west")
    print(a.throwlist())
