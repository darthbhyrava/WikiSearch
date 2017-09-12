import sys
from datetime import datetime
startTime = datetime.now()

def merge_d(d1, d2):
    union = {}
    for key in set(d1.keys()).union(d2.keys()):
        union[key] = []
        if key in d1 and key not in d2: # if the key is only in d1
            union[key] = d1[key]
        if key in d2 and key not in d1:
            union[key] = d2[key]
        if key in d1 and key in d2:
            union[key] = d1[key][:-1] + "+"+ d2[key]
    return union

start = 1
end = 2
all_dicts = []

for i in range(start, end+1):
    index_dict = {}
    i_file = open('./merged/mindex_%d' % i, 'r+')
    i_indices = i_file.readlines()
    for index in i_indices:
        if index == '\n':
            continue
        index_dict[index.split(':')[0]] = index.split(':')[1]
    i_file.close()
    all_dicts.append(index_dict)
    sys.stdout.write("\rIndexing: %d pages done." % (i))
    sys.stdout.flush()

print "\n", datetime.now() - startTime
print "Merging..."

while len(all_dicts) > 1:
    copy_all = all_dicts[:]
    all_dicts[:] = []
    c_len = len(copy_all)/2
    for ind in range(c_len):
        all_dicts.append(merge_d(copy_all[ind], copy_all[ind+c_len]))

fw = open("./merged/index_%d-%d" % (start, end), 'a+')
article_dict = sorted(all_dicts[0].items())
print "\n", datetime.now() - startTime
print "Writing to file..."
for key, value in article_dict:
    fw.write("%s:%s\n" % (key, value))
fw.close()
