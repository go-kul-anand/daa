def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    num = int(input("Enter element " + str(i+1) + ": "))
    arr.append(num)

target = int(input("Enter a number to be searched: "))
result = binary_search(arr, target)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
