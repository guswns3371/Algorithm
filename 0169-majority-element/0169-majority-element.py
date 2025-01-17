class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        snums = sorted(nums)
        return snums[len(snums) // 2]