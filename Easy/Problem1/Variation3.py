"""
Variation 3 - Naive Approach
Given an unsorted array of integers, find a pair with given sum in it
"""


def findpair(arr: list, sum: int) -> list:

    result = []
    # consider each element except last element
    for i in range(len(arr) - 1):
        # start from i'th element till last element
        for j in range(i + 1, len(arr)):

            # if desired sum is found, print it and return
            if arr[i] + arr[j] == sum:
                result.append(arr[i])
                result.append(arr[j])

    return result


if __name__ == '__main__':
    A = [8, 7, 2, 5, 3, 1]
    sum = 13

    print(findpair(A, sum))
