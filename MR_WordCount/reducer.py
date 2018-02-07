import sys

count_map = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    if word in count_map:
        count_map[word] += int(count)
    else:
        count_map[word] = int(count)

for word in count_map.keys():
    print "%s\t%s" % (word, count_map[word])