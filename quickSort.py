def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()  # Find pivot, pop() remove the last element and return

    items_greater = []  # store items greater than the pivot
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)  # if lower and or equal
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([5, 24, 6, 7, 2, 0, 1]))
