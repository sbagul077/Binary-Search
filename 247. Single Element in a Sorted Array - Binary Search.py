from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (mid + 1 == len(nums) or nums[mid + 1] != nums[mid]):
                return nums[mid]

            leftSide = mid - 1 if nums[mid] == nums[mid - 1] else mid
            # if leftSide % 2 is 0(False then we move low to mid + 1)
            # as if mid is at a even index means we have even values on the left
            # so we search right
            if leftSide % 2:
                high = mid - 1
            else:
                low = mid + 1

        return nums[low]


# Binary Search
# Time Complexity: O(logn)
# Space Complexity: O(1)


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNonDuplicate(nums))

# Bit Operator
# Time Complexity :O(n)
# Space Complexity:O(1)
