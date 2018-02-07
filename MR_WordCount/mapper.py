"""
Command to run :

        echo "foo bar foo bar abc" | Python mapper.py | sort | Python reducer.py
"""

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words:
        print "%s\t%s" % (word.lower(), 1)