# Takes an unsorted sequence and divides it into two sublists
# "sorted" and "unsorted". Sorted sublist will have length of one
# Take the leftmost element in unsorted list and move it into sorted list, if value of item to the left of new number is higher change positions of two items
# repeat

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1

    return list_a
