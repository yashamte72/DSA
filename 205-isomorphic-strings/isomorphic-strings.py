class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            hm1 = {}
            hm2 = {}

            for a,b in zip(s,t):
                if (a in hm1 and hm1[a] != b) or (b in hm2 and hm2[b] != a):
                    return False
                hm1[a] = b
                hm2[b] = a
            else:
                return True
        