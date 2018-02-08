import sys

word = None
current_word = None
current_count = 0

for line in sys.stdin:
    word, count = line.strip().split('\t', 1)
    if word == current_word:
        current_count += int(count)
    else:
        if current_word:
            print "%s\t%s" % (current_word, current_count)
        current_word = word
        current_count = int(count)

if current_word == word:
    print "%s\t%s" % (current_word, current_count)