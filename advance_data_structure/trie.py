from collections import defaultdict

def charToIdx(char):
    char = char.lower()
    return ord(char)-ord('a')

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if node.children[charToIdx(char)] is None:
                node.children[charToIdx(char)] = TrieNode()
            node = node.children[charToIdx(char)]
        node.is_word = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.children[charToIdx(char)] is None:
                return False
            node = node.children[charToIdx(char)]
        return node.is_word
    
if __name__ == "__main__":
    trie = Trie()
    trie.insert("Pankaj")
    trie.insert("Soni")
    trie.insert("a")
    print(f"Searching for 'Pankaj', {trie.search('Pankaj')}")
    print(f"Searching for 'Soni', {trie.search('Soni')}")
    print(f"Searching for 'sony', {trie.search('sony')}")

