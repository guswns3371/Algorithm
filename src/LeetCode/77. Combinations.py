"""
77. Combinations
https://leetcode.com/problems/combinations/
"""
from typing import List


class Solution:
    def __init__(self):
        self._k = None
        self._output = None
        self._nums = None

    def combine(self, n: int, k: int) -> List[List[int]]:
        self._k = k
        self._nums = [i for i in range(1, n + 1)]
        self._output = []
        self._BT(0, 0, [])
        return self._output

    def _BT(self, index: int, start: int, num_list: List[int]):
        if index == self._k:
            self._output.append(num_list.copy())
            return

        for i in range(start, len(self._nums)):
            c = self._nums[i]
            num_list.append(c)
            self._BT(index + 1, i + 1, num_list)
            num_list.pop()


solution = Solution()
print(solution.combine(4, 2))
print(solution.combine(5, 3))
