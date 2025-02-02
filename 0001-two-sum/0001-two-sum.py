class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx in range(len(nums)):
            num = nums[idx]
            needed = target - num
            if needed in num_map: # 진짜 이런 생각 어캐했누? 개천재들;;
                return [num_map[needed], idx]
            num_map[num] = idx
        