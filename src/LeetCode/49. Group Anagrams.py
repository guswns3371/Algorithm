"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = dict()
        for s in strs:
            now = tuple(sorted(s))
            if now not in data:
                data[now] = [s]
            else:
                data[now].append(s)
        return list(data.values())


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(sol.groupAnagrams(strs=[""]))
print(sol.groupAnagrams(strs=["a"]))
print(sol.groupAnagrams(strs=["ddddddddddg","dgggggggggg"]))
