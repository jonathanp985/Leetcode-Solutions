class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        right_sum = 0
        left_sum = 0
        
        vowels = set({'a', 'e', 'i', 'o', 'u'})

        for i in range((len(s) // 2), len(s)):

            if s[i].lower() in vowels:
                right_sum = right_sum + 1

            if s[len(s) - i - 1].lower() in vowels:
                left_sum = left_sum + 1

        return right_sum == left_sum
        