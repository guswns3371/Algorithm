class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def make(start, mask):
            if start >= n:
                return
            if mask in visit:
                return

            visit.add(mask)

            # make subset
            sub = []
            bits = f"{mask:0{n}b}"
            for i in range(n):
                if bits[i] == "1":
                    sub.append(nums[i])
            answer.append(sub)
            

            for i in range(start, n):
                make(i, mask ^ (1 << i))

        visit = set()
        n = len(nums)
        answer = []
        make(0, 0)
        return answer