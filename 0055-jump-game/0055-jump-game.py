class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        cur_idx = len(nums) - 1
        idx = cur_idx - 1
        while idx >= 0:
            if idx + nums[idx] >= cur_idx:
                cur_idx = idx
            idx -= 1
        return cur_idx == 0