"""
Variation 2 - Naive Approach
Returns the count of subarrays that add upto the target number
"""
from collections import defaultdict


def subArraySum(array, num, target):
    prevsum = defaultdict(int)
    res = 0
    currsum = 0

    for i in range(0, num):
        currsum += array[i]

        if currsum == target:
            res += 1

        if currsum - target in prevsum:
            res += prevsum[currsum - target]

        prevsum[currsum] += 1

    return res


if __name__ == '__main__':
    # arr = [10, 2, -2, -20, 10]
    arr = [1, 3, 5, 6, 1, 3, 9, 4]
    Sum = 12
    n = len(arr)

    print('Number of SubArrays: ', subArraySum(arr, n, Sum))
