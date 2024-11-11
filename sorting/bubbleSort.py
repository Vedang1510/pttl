def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = list(map(int, input("Enter numbers for Bubble Sort (space-separated): ").split()))
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)