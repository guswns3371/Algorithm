"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]", "", s).lower()
        n = len(s)
        print(s,n)
        if n % 2 == 0:
            return s[:n] == s[n::-1]
        else:
            return s[:n] == s[n + 1::-1]


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
print(sol.isPalindrome("a"))
print(sol.isPalindrome("abactcaba"))
print(sol.isPalindrome("0P"))
print(sol.isPalindrome("Never a foot too far, even."))
