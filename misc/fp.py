import feedparser
import urllib.request

d = feedparser.parse('http://export.arxiv.org/api/query?search_query=cat:cs.AI&id_list=&start=0&max_results=100')
count = 0
f = open("test.txt","w")
for entry in d.entries:
    f.write("###################[NEW ENTRY]#######################\n")
    f.write(entry.title)
    f.write("\n")
    f.write(entry.summary)
    f.write("\n\n")
    '''
    print(count)
    print(entry.title)
    print(entry.id)
    print(entry.arxiv_journal_ref)
    count +=1
    '''
f.close()


