
from __future__ import print_function
import sys
for line in sys.stdin:
    try: 
        year, tag_words=line.split("\t",1)
        for word in eval(tag_words):
            print(year+"\t"+word)
    except:
        next
    