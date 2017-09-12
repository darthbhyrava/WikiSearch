import sys

v_file = open('./merge_index/vocab','w+')
v_files = []
count = 0
for num in range(1,50):
    i_file = open('./indices/index_%d' % num, 'r+')
    index_list = i_file.readlines()
    for index in index_list:
        term = index.split(':')[0]
        if term not in v_files:
            v_files.append(term)
            count += 1
        sys.stdout.write("\rCounting: %d/49 files done, %d words found." % (num, count))
        sys.stdout.flush()
    i_file.close()


print ""
for v in v_files:
    v_file.write(v+"\n")
v_file.close()
