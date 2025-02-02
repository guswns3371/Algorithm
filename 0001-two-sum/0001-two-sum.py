class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx in range(len(nums)):
            num = nums[idx]
            if num not in num_map:
                num_map[num] = []
                
            num_map[num].append(idx)
            if len(num_map[num]) > 1 and num * 2 == target:
                return num_map[num][:2]
        
        sort_nums = sorted(num_map.keys())
        left = 0
        right = len(sort_nums) - 1
        while left < right:
            lnum, rnum = sort_nums[left], sort_nums[right]
            
            if lnum + rnum == target:
                return [num_map[lnum][0], num_map[rnum][0]]
            
            if lnum + rnum > target:
                right -= 1
            else:
                left += 1

        