import xml.etree.cElementTree as ET
from datetime import datetime
import sys

input_data = sys.argv[1]
startTime = datetime.now()
f = open("./output/output_0","a+")
article_count = 0
file_count = 0
title_dict = []
text_dict = []
write_flag = 0

for event, elem in ET.iterparse(file='%s' % input_data):
    if event == 'end':
        if elem.tag[-5:] == "title":
            if elem.text is None:
                elem.text = " "
            title_dict.append("<title>"+elem.text+"</title>")
        if elem.tag[-4:] == "text":
            if elem.text is None:
                elem.text = " "
            text_dict.append(elem.text)
            article_count += 1
            write_flag = 1

    if (article_count % 10000 == 0) and (write_flag == 1):
        for i in range(10000):
            text = title_dict[i].encode('utf-8') + text_dict[i].encode('utf-8') + "\n~~~~\n"
            f.write(text)
        f.close()

        write_flag = 0
        title_dict = []
        text_dict = []
        file_count += 1
        sys.stdout.write("\rReading: %d articles and %d blocks done." % (article_count, file_count))
        sys.stdout.flush()
        f = open(("./output/output_%s" % file_count), "a+")
    elem.clear()
