class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sstart = 0
        send = len(s) - 1
        tstart = 0
        tend = len(t) - 1

        while sstart < send and tstart < tend:
            if s[sstart] == t[tstart]:
                sstart += 1
            if s[send] == t[tend]:
                send -= 1
            
            tstart += 1
            tend -= 1
        
        if sstart == send:
            return s[sstart] in t[tstart: tend+1] 

        
        return sstart > send