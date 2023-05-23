class Solution:
    def NthRoot(self, n: int, m: int) -> int:
        # Write Your Code Here
        pass

        low = 0
        high = m

        def nthroot(mid: int, n: int) -> int:
            result = mid
            for i in range(1, n):
                result *= mid

            return result

        while low <= high:
            mid = low + (high - low) // 2
            curr = nthroot(mid, n)
            if curr == m:
                return mid
            elif curr > m:
                high = mid - 1
            else:
                low = mid + 1

        return -1

# Time Complexity: O(n) * O(logm)
# Space Complexity: O(1)


m = 27
n = 3
if __name__ == "__main__":
    obj = Solution()
    print(obj.NthRoot(n, m))
