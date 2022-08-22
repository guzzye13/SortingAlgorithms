# Faster than bubble sort.
def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)  # -1, once we know we have one item left
    # we don't need to do a comparison on it, we assume last item is the highest value.

    for i in indexing_length:
        min_value = i  # each iteration, first element will be default min

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:  # go to elements on the right, if we
                # find something smaller, min_value is changed.
                min_value = j

        if min_value != i:  # lower value than default than we switch.
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a


print(selection_sort([2,4,6,8,0,0,3,1,10]))