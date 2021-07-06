import urllib.request
import io
import sys

url = 'https://www.wikipedia.org/'


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, 'utf-8')
    return data.read()


f = open('robots.txt', 'w')
sys.stdout = f
print(get_robots_txt(url))
f.close()

