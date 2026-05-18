class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}

        if len(s1) > len(s2):
            return False  

        for i in range(len(s1)):
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            

        if s1_count == s2_count:
            return True

        L = 0
        for R in range(len(s1), len(s2)):
            s2_count[s2[R]] = s2_count.get(s2[R], 0) + 1
            s2_count[s2[L]] -= 1
            if s2_count[s2[L]] == 0:
                del s2_count[s2[L]]
            L += 1
            if s1_count == s2_count:
                return True

        return False
        