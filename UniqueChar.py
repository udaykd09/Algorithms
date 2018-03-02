from collections import defaultdict
from collections import Counter

def construct_freqs(string):
    freqs = defaultdict(lambda: 0)
    for char in string:
        freqs[char] += 1
    return freqs

def first_unique_char_1(string):
    freqs = construct_freqs(string)
    for ch in string:
        if freqs[ch] is 1:
            return ch
    return None

def first_unique_char_2(text):
    counters = Counter(text)
    for ch in text:
        if counters[ch] is 1:
            return ch

def firstUnique(string):
    for char in string:
        if string.count(char) == 1:
            return char

firstUnique("abcda")