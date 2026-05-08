class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            # Skip positive numbers (can't sum to 0)
            if nums[i] > 0:
                break

            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers
            L, R = i + 1, len(nums) - 1

            while L < R:
                total = nums[i] + nums[L] + nums[R]

                if total == 0:
                    result.append([nums[i], nums[L], nums[R]])
                    # Move both pointers inward
                    L += 1
                    R -= 1
                    # Skip duplicates for L and R
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

                elif total < 0:
                    L += 1   # Need bigger number

                else:
                    R -= 1   # Need smaller number

        return result
        