import bisect


# QuickSort ----------------------------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Merge Sort ---------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Insertion Sort -----------------------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Selection Sort -----------------------------------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


# Bubble Sort -----------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # The last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Python Sort -----------------------------------------------
def python_sort(arr):
    return sorted(arr)


# Tim Sort --------------------------------------------------
def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr)

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(
                left=arr[start:mid + 1],
                right=arr[mid + 1:end + 1]
            )
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr


# OG Sort ---------------------------------------------------
def og_sort(arr):
    if len(arr) <= 1:  # the list is already sorted
        return arr

    # step 1: The Grinding -> go through arr and remove all unordered elements, then put them, in order, inside ge
    ge = []  # ordered list of unordered elements inside arr
    elements_removed = 0  # the number of elements removed from arr up until current iteration (= len(ge))
    for i in range(1, len(arr)):  # we can skip the first element since it will be always sorted
        if arr[i-elements_removed] < arr[i-elements_removed - 1]:  # arr[i] < arr[i-1] -> the element is not in order
            ge.append(arr.pop(i-elements_removed))
            elements_removed += 1

    # step 2: The mix-taping-> go through ge and put every element at the right position inside arr
    elements_removed = 0  # the number of elements removed from ge up until current iteration (makes the index correct)
    for i in range(len(ge)):  # we can skip the first element since it will be always sorted
        bisect.insort(arr, ge.pop(i-elements_removed))
        elements_removed += 1

    return arr


def improved_og_sort(arr):
    if len(arr) <= 1:  # the list is already sorted
        return arr

    # step 1: The Grinding -> go through arr and remove all unordered elements, then put them, in order, inside ge
    ge = []  # ordered list of unordered elements inside arr
    elements_removed = 0  # the number of elements removed from arr up until current iteration (= len(ge))
    for i in range(1, len(arr)):  # we can skip the first element since it will be always sorted
        if arr[i-elements_removed] < arr[i-elements_removed - 1]:  # arr[i] < arr[i-1] -> the element is not in order
            bisect.insort(ge, arr.pop(i-elements_removed))
            elements_removed += 1

    # step 2: The mix-taping-> go through ge and put every element at the right position inside arr
    elements_removed = 0  # the number of elements removed from ge up until current iteration (makes the index correct)
    for i in range(len(ge)):  # we can skip the first element since it will be always sorted
        bisect.insort(arr, ge.pop(i-elements_removed))
        elements_removed += 1

    return arr


if __name__ == "__main__":
    array = [1, 3, 7, 2, 5, 7, 9, 1, 6]
    print(og_sort(array))
