class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted=sorted(nums)
        n=len(nums_sorted)
        i=0
        while i < n-1:
            if nums_sorted[i]==nums_sorted[i+1]:
                return True
            else: i+=1
        return False
        