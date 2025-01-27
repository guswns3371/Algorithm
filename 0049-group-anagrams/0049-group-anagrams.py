class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def make_key(word):
            key_list = [0 for _ in range(26)]
            for i in range(len(word)):
                key_list[ord(word[i]) % 26] += 1
            return ",".join(str(k) for k in key_list)


        ret = defaultdict(list)
        for word in strs:
            ret[make_key(word)].append(word)
        return list(ret.values())