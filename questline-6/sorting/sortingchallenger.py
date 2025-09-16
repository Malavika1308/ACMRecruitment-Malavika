def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
if __name__ == "__main__":
    test_list = [5, 2, 9, 1, 5, 6]  
    print("Original List:", test_list)
    sorted_list = bubble_sort(test_list)  
    print("Sorted List:", sorted_list)    
