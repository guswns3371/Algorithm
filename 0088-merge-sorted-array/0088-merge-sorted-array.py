class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = m + n - 1
        a = m - 1
        b = n - 1

        while a >= 0 and b >= 0:
            na = nums1[a]
            nb = nums2[b]
            nc = nums1[c]

            if nb >= na:
                nums1[c] = nb
                b -= 1
                c -= 1
            else:
                nums1[c] = na
                nums1[a] = nc
                a -= 1
                c -= 1

            # print(f"{na,nc,nb=} {c=}")
            # print(nums1, a)
            # print(nums2, b)
        
        while b >= 0:
            nums1[c] = nums2[b]
            c -= 1
            b -= 1


