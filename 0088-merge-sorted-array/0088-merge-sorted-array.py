class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        q = []
        a = 0
        b = 0
        
        while a < m and b < n:
            na = nums1[a]
            nb = nums2[b]

            if na <= nb:
                q.append(na)
                a += 1
            else:
                q.append(nb)
                b += 1
        if a < m:
            for i in range(a, m):
                q.append(nums1[i])
        if b < n:
            for i in range(b, n):
                q.append(nums2[i])
        for i in range(len(q)):
            nums1[i] = q[i]
