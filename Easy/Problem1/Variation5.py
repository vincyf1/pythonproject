"""
Variation 4 - Solution using Hashing
Given an unsorted array of integers, find a pair with given sum in it
Time Complexity == O(n)
"""


def findpair(A: list, sum: int) -> list:
    # Create an empty Hash map
    dict = {}
    result = []

    for i, e in enumerate(A):

        # Check if pair (e, sum - e) exists
        # if difference is seen before, print the pair

        if sum - e in dict:

            x = sum - e
            y = e

            print("Pair at index", dict.get(sum - e), "and ", i)

            result.append(x)
            result.append(y)

            return result

        dict[e] = i

    print("Pair not found")
    return []


if __name__ == '__main__':
    A = [8, 7, 2, 5, 3, 1]
    sum = 10

    print(findpair(A, sum))
