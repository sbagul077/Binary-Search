class Solution:
    def aggCows(self, arr, cows, n):
        arr.sort()
        low = 1
        high = arr[n - 1] - arr[0]

        while low <= high:
            mid = low + (high - low) // 2

            if self.canPlaceCows(arr, n, cows, mid):
                low = mid + 1
            else:
                high = mid - 1

        return high

    def canPlaceCows(self, arr: list[int], n: int, cows: int, mid: int) -> bool:
        cntCows = 1
        lastPlacedCow = arr[0]

        for i in range(1, n):
            if arr[i] - lastPlacedCow >= mid:
                cntCows += 1
                lastPlacedCow = arr[1]

        if cntCows >= cows:
            return True
        return False


if __name__ == "__main__":
    n = 5
    cows = 3
    arr = [1, 2, 8, 4, 9]
    obj = Solution()
    print(obj.aggCows(arr, cows, n))
