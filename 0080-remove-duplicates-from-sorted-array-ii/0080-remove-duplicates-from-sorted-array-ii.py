class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 2
        for i in range(2, len(nums)):
            current = nums[i]
            if nums[idx - 2] != current:
                nums[idx] = current
                idx += 1
        return idx
