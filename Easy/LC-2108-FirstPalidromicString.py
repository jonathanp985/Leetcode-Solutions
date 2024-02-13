class Solution:
    def isPalindrome(self, word):
        left, right = 0, len(word) - 1
        while(left < right):
            if word[left] != word[right]:
                return False
            left, right = left + 1, right - 1
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if self.isPalindrome(words[i]):
                return words[i]
        return ""
        