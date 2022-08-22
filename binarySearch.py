def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1

    return None


sequence_a = [2, 3, 4, 5, 5, 5, 0, 10]
item_a = 10
result = binary_search(sequence_a, item_a)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

