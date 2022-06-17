class Solution:
    def reverseWords(self, s: str) -> str:  
        wordsWithoutWhitespace = s.split() # ['the', 'sky', 'is', 'blue']
        reversedWords = wordsWithoutWhitespace[::-1] # ['blue', 'is', 'sky', 'the']        
        return " ".join(reversedWords)