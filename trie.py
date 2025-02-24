class Trie:

    def __init__(self):
        self.dict = {}
        # {"t": {"e": {"s": {"t": "\n"}}}

    def insert(self, word: str) -> None:
        # word = "test"
        #         ^
        # cur["t"] = {}
        cur = self.dict
        for char in word:
            if not char in cur:
                cur[char] = {}
            cur = cur[char]
        cur["\n"] = None  # end word

    def search(self, word: str) -> bool:
        cur = self.dict
        for char in word:
            if not char in cur:
                return False
            cur = cur[char]

        return "\n" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.dict
        for char in prefix:
            if not char in cur:
                return False
            cur = cur[char]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.dict)
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))