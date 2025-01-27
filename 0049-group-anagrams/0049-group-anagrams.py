class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            ret[key].append(word)
        return list(ret.values())