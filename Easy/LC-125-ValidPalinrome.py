class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s) - 1

        while front < back:

          if not s[front].isalnum():
            front += 1

          elif not s[back].isalnum():
            back -= 1 

          elif s[back].lower() == s[front].lower():
            front += 1
            back -= 1
            
          else:
            return False 

        return True