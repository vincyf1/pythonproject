# Algorithm: Selection Sort
# Order of Complexity: O(n^2)

def selection_sort(arr):
    start = 0

    while start < len(arr):
        for num in range(start, len(arr)):
            if arr[num] < arr[start]:
                arr[start], arr[num] = arr[num], arr[start]
        start += 1
        print(arr)


my_array = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(my_array)
