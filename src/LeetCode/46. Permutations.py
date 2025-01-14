"""
46. Permutations
https://leetcode.com/problems/permutations/
"""
from typing import List


class Solution:
    def __init__(self):
        self._nums = None
        self._output = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        self._nums = nums
        self._output = []
        self._BT(0, [])
        return self._output

    def _BT(self, index: int, num_list: List[int]):
        if index == len(self._nums):
            self._output.append(num_list.copy())
            return

        for c in self._nums:
            if c not in num_list:
                num_list.append(c)
                self._BT(index + 1, num_list)
                num_list.pop()


solution = Solution()
print(solution.permute(nums=[1, 2, 3]))
