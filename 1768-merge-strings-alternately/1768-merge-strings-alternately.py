class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        # Use zip to iterate through both simultaneously up to the shorter length
        for char1, char2 in zip(word1, word2):
            result.append(char1)
            result.append(char2)
        
        # Determine the length of the shorter word to slice the remainder
        min_len = min(len(word1), len(word2))
        
        # Append the rest of the longer string in one go
        result.append(word1[min_len:])
        result.append(word2[min_len:])
        
        return "".join(result)