class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Insert a word into the Trie and increase the prefix counts
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
    
    # Return the sum of prefix counts for all prefixes of the word
    def get_prefix_score(self, word):
        node = self.root
        total_score = 0
        for char in word:
            node = node.children[char]
            total_score += node.prefix_count
        return total_score

class Solution:
    def sumPrefixScores(self, words):
        trie = Trie()
        
        # Insert all words into the Trie
        for word in words:
            trie.insert(word)
        
        # Calculate the total score for each word
        result = []
        for word in words:
            result.append(trie.get_prefix_score(word))
        
        return result

# Example usage:
words1 = ["abc", "ab", "bc", "b"]
words2 = ["abcd"]
sol = Solution()
print(sol.sumPrefixScores(words1))  # Output: [5, 4, 3, 2]
print(sol.sumPrefixScores(words2))  # Output: [4]
