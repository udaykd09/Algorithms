class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c = {}
        self.word = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return None
        for l in word:
            if l not in self.c:
                self.c[l] = Trie()
            self = self.c[l]
        self.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        for l in word:
            if l not in self.c:
                return False
            self = self.c[l]
        return self.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for p in prefix:
            if p not in self.c:
                return False
            self = self.c[p]
        return self != None


#Your Trie object will be instantiated and called as such:
obj = Trie()
word = "word"
obj.insert(word)
print obj.search(word)
print obj.startsWith("p")