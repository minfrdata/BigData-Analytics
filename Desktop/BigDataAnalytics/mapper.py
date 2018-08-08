

import sys
for line in sys.stdin.readlines():
    try: 
        year, tag_words=line.split("\t",1)
        for word in eval(tag_words):
            sys.stdout.write("{}\t{}\n".format(year,word))
    except:
        next
    
