class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Step 1: Build left products
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Step 2: Build right products
        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Step 3: Multiply left and right
        output = [1] * n
        for i in range(n):
            output[i] = left[i] * right[i]

        return output