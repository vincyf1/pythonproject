"""
Variation 1 - Naive Approach
Given an unordered array and a target, find a continuous subarray whose sum is equal to the target
nums = 10 2 5 7 1 3 9 4
target = 12
"""

arr = [1, 3, 5, 6, 1, 3, 9, 4]


def findPair(nums: list, target: int) -> list:
    result = []
    for x in range(len(nums)):
        result.append(arr[x])
        while sum(result) > target:
            result.pop(0)
        if sum(result) == target:
            return result
    return []


print(findPair(arr, 15))
