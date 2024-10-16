
def binarySearch(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        # Calculate mid each time inside the loop
        mid = (left + right) // 2

        # Check if the mid element is the target
        if lst[mid] == target:
            return mid
        # If the target is greater, ignore the left half
        elif lst[mid] < target:
            left = mid + 1
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    return -1  # Target not found

# Example usage
lst = [45, 56, 78, 89, 94, 96]  # Make sure the list is sorted
target = 94

ans = binarySearch(lst, target)
if ans != -1:
    print("Element found at index:", ans)
else:
    print("Element not found in the list")




