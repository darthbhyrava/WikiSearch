import sys

for i in range(1563,1764):
    i_file = open('./Indices/index_%d' % i, 'r+')
    pairs = i_file.readlines()
    for pair in pairs:
        term = pair.split(':')[0]
        index = pair.split(':')[1]
        w_file = open('./vocab/%s' % term, 'a+')
        w_file.write("+"+index)
        w_file.close()
        sys.stdout.write("\r %d words done." % (i))
        sys.stdout.flush()
    i_file.close()
