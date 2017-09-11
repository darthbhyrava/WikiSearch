#makes a count list from the output files, for accurate indexing
import sys

count = 0
f = open('count_list','a+')
for i in range(1765):
    old_count = count
    fr = open("./output/output_%d" % i)
    content = fr.read()
    article_list = content.split('~~~~')
    count += len(article_list)
    entry = ("%d: [%d, %d]" % (i, old_count, count))+"\n"
    f.write(entry)
    sys.stdout.write("\rCounting: %d blocks done." % (i))
    sys.stdout.flush()
    fr.close()
f.close()
