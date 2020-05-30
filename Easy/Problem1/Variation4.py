"""
Variation 4 - Solution using Sorting
Given an unsorted array of integers, find a pair with given sum in it
Time Complexity == O(nlog(n))
"""


def findpair(A: list, sum: int) -> list:
    result = []
    A.sort()

    (low, high) = (0, len(A)-1)

    while low < high:
        if A[low] + A[high] == sum:
            result.append(A[low])
            result.append(A[high])
            return result

        if A[low] + A[high] < sum:
            low += 1
        else:
            high -= 1

    print("No Pair found")
    return []


if __name__ == '__main__':

    A = [8, 7, 2, 5, 3, 1]
    Sum = 15

    print(findpair(A, Sum))
