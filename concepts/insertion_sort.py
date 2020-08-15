# Algorithm: Insertion Sort
# Order of Complexity: O(n^2)

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    print(arr)


my_array = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
insertion_sort(my_array)
