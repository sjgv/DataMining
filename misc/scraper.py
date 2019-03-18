import urllib.request
import feedparser
url = 'http://export.arxiv.org/api/query?search_query=cs'
with urllib.request.urlopen(url) as url:
    d = url.read()
    feed = atoma.parse_atom_bytes(d)
    for t in feed.title.value:
        print(t)
