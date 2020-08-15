# Algorithm: Bubble Sort
# Order of Complexity: O(n^2)

def bubble_sort(arr):
    swap_flag = True

    while swap_flag:
        swap_flag = False
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                swap_flag = True
                arr[num], arr[num + 1] = arr[num + 1], arr[num]
    print(arr)


my_array = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(my_array)
