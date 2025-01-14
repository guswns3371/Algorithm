"""
344. Reverse String
https://leetcode.com/problems/reverse-string/
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]


sol = Solution()
print(sol.reverseString(["h", "e", "l", "l", "o"]))
print(sol.reverseString(["H", "a", "n", "n", "a", "h"]))
