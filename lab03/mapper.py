#!/opt/anaconda/envs/bd9/bin/python

#* Third lab, Alexander Medvedev

import sys
import re
from urllib.parse import urlparse, unquote

def emit(key, value):
    print(key,value)
    #sys.stdout.write("{}\t{}\n".format(key,value))

def mapper(uid, url):
    emit(uid,url2domain(url))
    

def map():
    for line in sys.stdin:
        obj = line.strip().split("\t")
        if len(obj) > 2:
            mapper(obj[0],obj[2])

def url2domain(url):
   try:
       a = urlparse(unquote(url.strip()))
       if (a.scheme in ['http','https']):
           b = re.search("(?:www\.)?(.*)",a.netloc).group(1)
           if b is not None:
               return str(b).strip()
           else:
               return ''
       else:
           return ''
   except:
       return

if __name__ == "__main__":
    map()
