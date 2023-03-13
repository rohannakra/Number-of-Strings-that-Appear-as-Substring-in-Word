# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

def num_of_strings(patterns, word):
    counter = 0

    for pattern in patterns:
        if pattern in word:
            counter += 1
    
    return counter

print(num_of_strings(["a","abc","bc","d"], 'abc'))
print(num_of_strings(['a', 'b', 'c'], "aaaaabbbbb"))
print(num_of_strings(['a', 'a', 'a'], 'ab'))

# -------------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0

        for pattern in patterns:
            if pattern in word:
                counter += 1
    
        return counter
