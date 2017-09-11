from datetime import datetime
from Stemmer import Stemmer
from stop_words import get_stop_words
import nltk
import re
import sys

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def merge_d(d1, d2):
    union = {}
    for key in set(d1.keys()).union(d2.keys()):
        union[key] = []
        if key in d1 and key not in d2: # if the key is only in d1
            union[key] = d1[key]
        if key in d2 and key not in d1:
            union[key] = d2[key]
        if key in d1 and key in d2:
            union[key] = d1[key] + "+"+ d2[key]
    return union

startTime = datetime.now()
stop_words = get_stop_words('en')
p_stemmer = Stemmer('english')
start = 900
end = 902


c = open('count_list', 'r+')
lines = c.readlines()
c.close()

for i in range(start,end):
    all_dicts = []
    pair = lines[i].split(':')
    file_num = int(pair[0])+1
    count = int(pair[1].split(',')[0].strip().replace('[','')) + 1
    i_count = count
    input_file = "./output/output_%d" % file_num
    output_file = "./indices/index_%d" % file_num
    fr = open('%s' % input_file, 'r+')
    fw = open('%s' % output_file, 'a+')
    content = fr.read().split('~~~~')

    for text in content:
        #getting title
        title = find_between(text, "<title>", "</title>")
        text = text.replace(title, '')
        #getting infobox
        info = find_between(text, "{{Infobox", "}}")
        text = text.replace(info, '')
        #getting categories
        cats = re.findall(r'\[\[Category:([^]]*)\]\]', text)
        for i in cats:
            text = text.replace(i, '')
        #getting external links
        extl = find_between(text, "xternal links==", "\n\n")
        text = text.replace(extl, '')
        #getting references
        ref = find_between(text, "eferences==", "==") + find_between(text, "eferences ==", "==")
        text = text.replace(ref, '')

        #clearing up the dictionary, and working on each field
        article_dict = {}

        #TITLE
        field_tokens = []
        title = re.sub('[^A-Za-z]', ' ', title)
        chunk = nltk.word_tokenize(title.lower())
        stopped_tokens = [i for i in chunk if not i in stop_words]
        field_tokens = p_stemmer.stemWords(stopped_tokens)
        for i in field_tokens:
            if i in article_dict.keys():
                freq = int(find_between(article_dict[i], "(",")")) + 1
                if "T" in article_dict[i]:
                    article_dict[i] = find_between(article_dict[i], "", "(") + "(%d)" % freq
                else:
                    article_dict[i] = "T" + find_between(article_dict[i], "", "(") + "(%d)" % freq
            else:
                article_dict[i] = "T%d(1)" % count

        #BODY TEXT
        field_tokens = []
        text = re.sub('[^A-Za-z]', ' ', text)
        chunk = nltk.word_tokenize(text.lower())
        stopped_tokens = [i for i in chunk if not i in stop_words]
        field_tokens = p_stemmer.stemWords(stopped_tokens)
        for i in field_tokens:
            if i in article_dict.keys():
                freq = int(find_between(article_dict[i], "(",")")) + 1
                if "B" in article_dict[i]:
                    article_dict[i] = find_between(article_dict[i], "", "(") + "(%d)" % freq
                else:
                    article_dict[i] = "B" + find_between(article_dict[i], "", "(") + "(%d)" % freq
            else:
                article_dict[i] = "B%d(1)" % count

        # INFOBOX
        field_tokens = []
        info = re.sub('[^A-Za-z]', ' ', info)
        chunk = info.lower()
        chunk = nltk.word_tokenize(chunk)
        stopped_tokens = [i for i in chunk if not i in stop_words]
        field_tokens = p_stemmer.stemWords(stopped_tokens)
        for i in field_tokens:
            if i in article_dict.keys():
                freq = int(find_between(article_dict[i], "(",")")) + 1
                if "I" in article_dict[i]:
                    article_dict[i] = find_between(article_dict[i], "", "(") + "(%d)" % freq
                else:
                    article_dict[i] = "I" + find_between(article_dict[i], "", "(") + "(%d)" % freq
            else:
                article_dict[i] = "+I%d(1)" % count

        # CATEGORIES
        field_tokens = []
        cat = " ".join(cats)
        cat = re.sub('[^A-Za-z]', ' ', cat)
        chunk = cat.lower()
        chunk = nltk.word_tokenize(chunk)
        stopped_tokens = [i for i in chunk if not i in stop_words]
        field_tokens = p_stemmer.stemWords(stopped_tokens)
        for i in field_tokens:
            if i in article_dict.keys():
                freq = int(find_between(article_dict[i], "(",")")) + 1
                if "C" in article_dict[i]:
                    article_dict[i] = find_between(article_dict[i], "", "(") + "(%d)" % freq
                else:
                    article_dict[i] = "C" + find_between(article_dict[i], "", "(") + "(%d)" % freq
            else:
                article_dict[i] = "C%d(1)" % count

        # REFERENCES
        field_tokens = []
        ref = re.sub('[^A-Za-z]', ' ', ref)
        chunk = ref.lower()
        chunk = nltk.word_tokenize(chunk)
        stopped_tokens = [i for i in chunk if not i in stop_words]
        field_tokens = p_stemmer.stemWords(stopped_tokens)
        for i in field_tokens:
            if i in article_dict.keys():
                freq = int(find_between(article_dict[i], "(",")")) + 1
                if "R" in article_dict[i]:
                    article_dict[i] = find_between(article_dict[i], "", "(") + "(%d)" % freq
                else:
                    article_dict[i] = "R" + find_between(article_dict[i], "", "(") + "(%d)" % freq
            else:
                article_dict[i] = "R%d(1)" % count

        # EXTERNAL LINKS
        field_tokens = []
        extl = re.sub('[^A-Za-z]', ' ', extl)
        chunk = extl.lower()
        chunk = nltk.word_tokenize(chunk)
        stopped_tokens = [i for i in chunk if not i in stop_words]
        field_tokens = p_stemmer.stemWords(stopped_tokens)
        for i in field_tokens:
            if i in article_dict.keys():
                freq = int(find_between(article_dict[i], "(",")")) + 1
                if "E" in article_dict[i]:
                    article_dict[i] = find_between(article_dict[i], "", "(") + "(%d)" % freq
                else:
                    article_dict[i] = "E" + find_between(article_dict[i], "", "(") + "(%d)" % freq
            else:
                article_dict[i] = "E%d(1)" % count

        count += 1
        sys.stdout.write("\rIndexing: %d pages done." % (count-i_count))
        sys.stdout.flush()
        all_dicts.append(article_dict)


    print "\nMerging..."

    while len(all_dicts) > 1:
        copy_all = all_dicts[:]
        all_dicts[:] = []
        c_len = len(copy_all)/2
        for ind in range(c_len):
            all_dicts.append(merge_d(copy_all[ind], copy_all[ind+c_len]))

    print  "Writing indices..."

    article_dict = sorted(all_dicts[0].items())
    for key, value in article_dict:
        fw.write("%s:%s\n" % (key, value))
    fw.close()
    fr.close()

    print datetime.now() - startTime
    print "Indexing done till block numbers: %d. Progress: %d/300." % (file_num, (file_num-start))
