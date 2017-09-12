from math import log10
import sys
from pygtrie import CharTrie
from datetime import datetime
startTime = datetime.now()

doc_num = 17702850
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

tr = CharTrie()
for i in range(3,9):
    f = open('./merged/mindex_%d' % i,'r+')
    indices = f.readlines()
    tr.clear()
    l_len = len(indices)
    for ind, index in enumerate(indices):
        if index == '\n':
            continue
        term = index.split(':')[0]
        index_val = index.split(':')[1]
        doc_list = index_val.split('+')
        idf = log10(float(doc_num)/float(len(doc_list)))
        tr[term] = str(ind+1) + ", " + str(idf)
        sys.stdout.write("\rIndexing: %d/%d done - %d block..." % (ind+1, l_len, i))
        sys.stdout.flush()
    g = open('./tries/trie_%d' % i,'a+')
    print "Writing to file ..."
    for i,j in tr.items():
        g.write(i+" "+str(j)+"\n")
    g.close()
    f.close()
    print datetime.now() - startTime
