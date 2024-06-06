def partition(arr, low, high, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = median_of_medians(arr, low, high)
    pivot_index = partition(arr, low, high, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select(arr, low, pivot_index - 1, k)
    else:
        return select(arr, pivot_index + 1, high, k)

def median_of_medians(arr, low, high):
    n = high - low + 1
    if n < 5:
        sorted_arr = sorted(arr[low:high + 1])
        return low + sorted_arr.index(sorted_arr[n // 2])

    medians = []
    for i in range(low, high + 1, 5):
        group = sorted(arr[i:min(i + 5, high + 1)])
        medians.append(group[len(group) // 2])

    median_of_medians_index = median_of_medians(medians, 0, len(medians) - 1)
    return arr.index(medians[median_of_medians_index])

def bfprt(arr, k):
    return select(arr, 0, len(arr) - 1, k - 1)

def main():
    # Tests
    arr1 = [3, 2, 1, 5, 4]
    arr2 = [10, 4, 5, 8, 6, 11, 26]
    arr3 = [7, 10, 4, 3, 20, 15]

    print("Test 1:")
    k1 = 3
    result1 = bfprt(arr1, k1)
    print(f"The {k1}-th smallest element in {arr1} is {result1}")
    assert result1 == 3, f"Test 1 failed, expected 3 but got {result1}"

    print("Test 2:")
    k2 = 5
    result2 = bfprt(arr2, k2)
    print(f"The {k2}-th smallest element in {arr2} is {result2}")
    assert result2 == 10, f"Test 2 failed, expected 10 but got {result2}"

    print("Test 3:")
    k3 = 2
    result3 = bfprt(arr3, k3)
    print(f"The {k3}-th smallest element in {arr3} is {result3}")
    assert result3 == 4, f"Test 3 failed, expected 4 but got {result3}"

    print("All tests passed!")

if __name__ == "__main__":
    main()