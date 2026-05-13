class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Edge case: empty array
        if not nums:
            return 0

        # Step 1: sort the array
        nums.sort()

        longest = 1
        length  = 1

        # Step 2: scan once
        for i in range(1, len(nums)):

            # Case 1: consecutive number
            if nums[i] == nums[i-1] + 1:
                length += 1
                longest = max(longest, length)

            # Case 2: duplicate → skip
            elif nums[i] == nums[i-1]:
                continue

            # Case 3: gap → reset
            else:
                length = 1

        return longest