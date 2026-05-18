class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        str1 = sorted(s1)         
        l    = 0

        for r in range(len(s1), len(s2) + 1):

            window = s2[l : l + len(s1)]   
            if str1 == sorted(window):      
                return True

            l += 1                          

        return False


        