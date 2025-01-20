def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


numbers = [2, 4, 6, 8, 10, 12, 14]
target = 2

result = binary_search(numbers, target)

print(f"Индекс числа = {result}")
