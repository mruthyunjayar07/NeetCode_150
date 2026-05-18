class TrieNode:
    def __init__(self):
        self.children = [None] * 26   # a-z
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()        # ✅ now root exists

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return cur.endOfWord          # must be a complete word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return True                   # any node existing = prefix found