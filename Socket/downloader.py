
from threading import Thread
import urllib.request as urllib
import urllib.parse as urlparse
from bs4 import BeautifulSoup
# sudo pip3 install beautifulsoup4
# https://codeshare.io/5zlBDk

def download(url, filename):
    response = urllib.urlopen(url)
    source = response.read()

    with open(filename, 'wb') as file:
        file.write(source)

def imageDownload(url):
    response = urllib.urlopen(url)
    source = response.read()

    soup = BeautifulSoup(source)

    td_list = soup.findAll( 'img' )
    for td in td_list:
        path = urlparse.urljoin(url, td['src'])
        filename = (td['src'].split('/')[-1])

        download(path, filename)

def folder_downloader(url):
    response = urllib.urlopen(url)
    source = response.read()

    soup = BeautifulSoup(source, "html.parser")
    tr_list = soup.findAll( 'tr' )

    for tr in tr_list:
        img = tr.find('img', {'alt': True})

        if img and img['alt'] == '[DIR]' and not img['src'].endswith('back.gif'):
            a = tr.find('a')
            path = urlparse.urljoin(url, a['href'])

            thread_download = Thread(target=folder_downloader, args=(path,))
            thread_download.start()

        if img and img['alt'] == '[   ]':
            a = tr.find('a')

            path = urlparse.urljoin(url, a['href'])
            filename = a['href'].split('/')[-1]

            thread2 = Thread(target=download, args=(path, filename))
            thread2.start()

folder_downloader('http://indir.istihza.com')
