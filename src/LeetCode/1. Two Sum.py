"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i, n in enumerate(nums):
            data = target - n
            if data in hash_map:
                return [i, hash_map[data]]
            hash_map[n] = i


sol = Solution()
print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
print(sol.twoSum(nums=[3, 2, 4], target=6))
print(sol.twoSum(nums=[3, 3], target=6))
