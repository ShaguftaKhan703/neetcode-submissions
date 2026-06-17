class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:
                # Is target in the sorted left half?
                if nums[low] <= target < nums[mid]:
                    high = mid - 1   # ✓ search left
                else:
                    low = mid + 1    # ✗ search right

            # Right half is sorted
            else:
                # Is target in the sorted right half?
                if nums[mid] < target <= nums[high]:
                    low = mid + 1    # ✓ search right
                else:
                    high = mid - 1   # ✗ search left

        return -1
        