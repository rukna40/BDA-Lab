def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    
    while l <= r:
        m = (l + r) // 2
        
        if arr[m] == x:
            return m
        
        elif arr[m] < x:
            l = m + 1
        
        else:
            r = m - 1
    
    return -1

arr = [2, 3, 4, 10, 40]
x = 10

ind = search(arr, x)

if ind != -1:
    print(f"Element found at index {ind}")
else:
    print("Element not found in array")
