class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # Count zeros and get total product (ignoring zeros)
        zero_count = nums.count(0)
        total = 1
        for num in nums:
            if num != 0:
                total *= num

        output = []
        for num in nums:

            # Case 1: more than one zero → everything is 0
            if zero_count > 1:
                output.append(0)

            # Case 2: exactly one zero
            elif zero_count == 1:
                if num == 0:
                    output.append(total)   # only this index gets total
                else:
                    output.append(0)       # rest all get 0

            # Case 3: no zeros → normal division
            else:
                output.append(total // num)

        return output