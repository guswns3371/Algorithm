"""
937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/
"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        slist = []
        nlist = []
        for log in logs:
            data = log.split()
            if data[1].isnumeric():
                nlist.append(data)
            else:
                slist.append(data)
        slist.sort(key=lambda x: (x[1:], x[0]))
        return [" ".join(x) for x in slist + nlist]


sol = Solution()
print(sol.reorderLogFiles(logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
print(sol.reorderLogFiles(logs=["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
