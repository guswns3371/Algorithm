"""
78. Subsets
https://leetcode.com/problems/subsets/
"""
from typing import List


class Solution:
    def __init__(self):
        self._output = None
        self._nums = None

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self._nums = nums
        self._output = []
        self._BT(0, [])
        return self._output

    def _BT(self, index: int, nums: List[int]):
        if index == len(self._nums):
            self._output.append(nums.copy())
            return

        num = self._nums[index]
        nums.append(num)
        self._BT(index + 1, nums)
        nums.pop()
        self._BT(index + 1, nums)


solution = Solution()
print(solution.subsets(nums=[1, 2, 3]))
