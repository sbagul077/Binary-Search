def getMedian(matrix):
    # Write your code here.
    pass
    low = matrix[0][0]
    high = 0
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][-1])

    while low <= high:
        mid = low + (high - low) // 2
        count = 0
        for i in range(len(matrix)):
            count += lessThanMid(matrix[i], mid)

        if count <= (n * m) // 2:
            low = mid + 1
        else:
            high = mid - 1

    return low


def lessThanMid(row, mid):
    result = 0

    for r in row:
        if r <= mid:
            result += 1
        elif r > mid:
            break
    return result
