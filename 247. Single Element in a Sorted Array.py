from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result = result ^ num

        return result


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

if __name__ == "__main__":
    obj = Solution()
    print(obj.singleNonDuplicate(nums))

# Bit Operator
# Time Complexity :O(n)
# Space Complexity:O(1)
