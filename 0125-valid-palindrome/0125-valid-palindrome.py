class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            a = s[start]
            b = s[end]

            if not a.isalnum():
                start += 1
                continue
            if not b.isalnum():
                end -= 1
                continue

            alow = a.lower()
            blow = b.lower()
            if alow != blow:
                return False
            start += 1
            end -= 1

        return start >= end
