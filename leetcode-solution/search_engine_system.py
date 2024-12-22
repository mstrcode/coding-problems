from typing import List
# Approach 1: Fruteforce - Sort, and search for all
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Assuming products is already sorted lexicographically
        products.sort()
        suggestions = []
        for ci in range(len(searchWord)):
            l = list(filter(lambda s: s.startswith(searchWord[:ci+1]), products))
            suggestions.append(l[:3])
        return suggestions
    
## Approach 2:
# 1. Sort the products
# for all the prefix in search word
#   binary_search(products, prefix)
# 
class Solution2:
    def prefixBS(self, array: List[str], prefix: str) -> List[str]:
        left = 0; right = len(array)-1
        
        
        while left <= right:
            # print(left, right, prefix)
            mid = (left + right) // 2
            mid_word_pf = array[mid][:len(prefix)+1]
            if mid_word_pf > prefix:
                right = mid-1
            elif mid_word_pf < prefix:
                left = mid+1
            else:
                if mid==0:
                    return array[:3]
                elif array[mid-1][:len(prefix)+1]==prefix:
                    right = mid - 1
                else:
                    return array[mid: mid+3]
        
        if left < len(array):
            # print(array[left:left+3])
            return array[left:left+3]
        else:
            return []



    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Assuming products is already sorted lexicographically
        products.sort()
        # print(products)
        suggestions = []
        for ci in range(len(searchWord)):
            output = []
            l = self.prefixBS(products, searchWord[:ci+1])
            l = list(filter(lambda x: x.startswith(searchWord[:ci+1]), l))
            suggestions.append(l)


        return suggestions
           
## Approach 3:
# Use trie for prefix
def charToIdx(char):
    return ord(char)-ord('a')

class TrieNode:
    def __init__(self):
        self.children = [None]*26 # as the letters are only lower, we consider only 26 characters possibility
        self.suggestions = [] # Max 3 suggestions will be recorded while building trie
        self.is_completed = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.children[charToIdx(char)] is None:
                # char is not present in trie
                # so insert it
                node.children[charToIdx(char)] = TrieNode()
            node = node.children[charToIdx(char)]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
        node.is_completed = True
        
        

    


class Solution3:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        output = []
        node = trie.root
        for char in searchWord:
            if node:
                node = node.children[charToIdx(char)]
            if node:
                output.append(node.suggestions)
            else:
                output.append([])
        return output



        