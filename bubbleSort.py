def bubble(list_a):  # sorted list
    indexing_length = len(list_a) - 1  # where we make comparisons
    sort = False  # Variable to let us know when the array has been sorted

    while not sort:  # While sorted is False do the actions
        sort = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sort = False  # Once done sort is True ending the while loop.
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]  # Swap
    return list_a


print("Bubble Sort: ", bubble([3, 4, 0, 9, 8, 7]))
