class Solution:
    def kthElement(self, nums1, nums2, k):

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.kthElement(nums2, nums1, k)

        low = max(0, k - n2)
        high = min(k, n1)

        while low <= high:
            partX = low + (high - low) // 2
            partY = k - partX

            L1 = float("-inf") if partX == 0 else nums1[partX - 1]
            R1 = float("inf") if partX == n1 else nums1[partX]
            L2 = float("-inf") if partY == 0 else nums2[partY - 1]
            R2 = float("inf") if partY == n2 else nums2[partY]

            if L1 <= R2 and L2 <= R1:
                return max(L1, L2)
            elif L1 > R2:
                high = partX - 1
            else:
                low = partX + 1

        return 0


# Binary Search
# Time Complexity : log(min(m,n))
# Space Complexity : O(1)
#

nums1 = [100, 112, 256, 349, 770]
nums2 = [72, 86, 113, 119, 265, 445, 892]
k = 7

if __name__ == "__main__":
    obj = Solution()
    print(f"{obj.kthElement(nums1, nums2, k)} is the {k} largest element")
