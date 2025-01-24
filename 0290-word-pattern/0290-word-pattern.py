class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pmap = {}
        smap = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        for i in range(len(s)):
            pw = pattern[i]
            sw = s[i]

            if pw not in pmap:
                pmap[pw] = sw
            if sw not in smap:
                smap[sw] = pw

            if pmap[pw] != sw or smap[sw] != pw:
                return False
        return True
