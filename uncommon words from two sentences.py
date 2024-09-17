from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1, s2):
        # Split both sentences into words
        words1 = s1.split()
        words2 = s2.split()

        # Count occurrences of words in both sentences
        word_count = Counter(words1 + words2)

        # Find the uncommon words
        uncommon_words = [word for word, count in word_count.items() if count == 1]

        return uncommon_words

# Example usage:
# Instantiate the Solution class
solution = Solution()

# Test cases
s1_1 = "this apple is sweet"
s2_1 = "this apple is sour"
s1_2 = "apple apple"
s2_2 = "banana"

# Running the method and printing the results
print(solution.uncommonFromSentences(s1_1, s2_1))  # Output: ['sweet', 'sour']
print(solution.uncommonFromSentences(s1_2, s2_2))  # Output: ['banana']
