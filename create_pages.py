import envoy
import csv
import sys

def create_page(files, page, cropstring="'763x1040+3569+0'", w=3):
    print files
    for f in files:
        dpi = 300
        envoy.run("inkscape -D -d={1} -e=tmp/{0}.png {0}".format(f, dpi))
        #envoy.run("convert -crop {1} tmp/o_{0}.png tmp/{0}.png".format(f, cropstring))
    
    l = len(files)
    for i in range(0,(l+w-1)/w):
        s = " ".join("tmp/{0}.png".format(files[w*i+j]) 
                for j in range(0, min(w, l-w*i)))
        envoy.run("convert {0} +append tmp/row{1}.png".format(s, i))
    s = " ".join("tmp/row{0}.png".format(i) for i in range(0, min(w, (l+w-1)/w)))
    envoy.run("convert {0} -append pages/page{1}.png".format(s, page))

def create_pages(cards, p=0, cropstring=None, w=3):
    w2 = w*w
    l = (len(cards) + w2 - 1) / (w2)
    for i in range(0, l):
        create_page(cards[w2*i:w2*i+w2], i+p, cropstring, w)
    return l+p

cards = sys.argv[1:]

create_pages(cards, w=3)
