# Algorithm: Merge Sorted Array
# Order of Complexity: O(nlog(n))

# Merge Sorted Lists
def merge_sorted(arr1, arr2):
    print("Merge function called with lists below")
    print(f"Left: {arr1} and Right: {arr2}")
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
        print(sorted_arr)

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
        print(sorted_arr)

    return sorted_arr


list1 = [2, 4, 6, 8, 10, 11, 12]
list2 = [1, 3, 5, 7, 8, 9, 13]
print(f"Merged list: {merge_sorted(list1, list2)}")
