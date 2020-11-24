# Takes an un ordered list and sorts them in ascending value
# Compares two values at any given time.
# loops through lists and sorts it

def bubble_sort(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a

print(bubble_sort([1,3,565,4543,434,767,67897,87,34]))