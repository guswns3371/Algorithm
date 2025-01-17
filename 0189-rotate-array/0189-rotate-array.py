class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        front_nums = nums[n - k:]
        last_index = n - 1
        for i in range(n - k):
            nums[last_index - i] = nums[last_index - i - k]
        for i in range(k):
            nums[i] = front_nums[i]