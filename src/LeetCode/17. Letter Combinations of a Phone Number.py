"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def __init__(self):
        self._keypad = None
        self._digits = None
        self._comb = None

    def letterCombinations(self, digits: str) -> List[str]:
        self._keypad = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if len(digits) == 0:
            return []

        self._digits = digits
        self._comb = []
        self._BT(index=0, crntStr=[])
        return self._comb

    def _BT(self, index: int, crntStr: List[str]):
        if index >= len(self._digits):
            self._comb.append("".join(crntStr))
            return

        num = int(self._digits[index])
        chars = self._keypad[num]
        for c in chars:
            crntStr.append(c)
            self._BT(index + 1, crntStr)
            crntStr.pop()


letterComb = Solution()
print(letterComb.letterCombinations(digits="259"))
