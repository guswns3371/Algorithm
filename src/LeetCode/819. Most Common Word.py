"""
819. Most Common Word
https://leetcode.com/problems/most-common-word/
"""
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        data = ""
        for p in paragraph:
            if p.isalpha():
                data += p
            else:
                data +=" "
        data = [x for x in data.split() if x not in banned]
        count = Counter(data)
        return count.most_common(1)[0][0]


sol = Solution()
print(sol.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"]))
print(sol.mostCommonWord(paragraph="a.", banned=[]))
print(sol.mostCommonWord(paragraph="a, a, a, a, b,b,b,c, c", banned= ["a"]))
