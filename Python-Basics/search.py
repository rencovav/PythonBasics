# linear search
def linear_search(list, n, key):
    for i in range(0, n):
        if list[i] == key:
            return i
    return -1


numbers = [1, 3, 5, 4, 7, 9]
searched_element = 7

length = len(numbers)

response = linear_search(numbers, length, searched_element)

if response == -1:
    print("Element not found")
else:
    print("Element found at index: ", response)


# binary search
def binary_search(list, n):
    low = 0
    high = len(list_numbers) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if list_numbers[mid] < n:
            low = mid + 1

        elif list_numbers[mid] > n:
            high = mid - 1

        else:
            return mid

    return -1


list_numbers = [12, 24, 32, 39, 45, 50, 54]
searched = 45

result = binary_search(list_numbers, searched)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in the list")
