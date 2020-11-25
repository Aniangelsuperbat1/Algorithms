# find minimum value in a list
# set first number as the minmum and compare every number to the right
# when you come across a number lower than the minimum, this number becomes the new minimum and you continue through the list
# at the end of the itteration the new minimum value will be moved to the left
# new list will be sorted into two lists. List on the left will be sorted and list on the right will be unsorted
# repeat until list is sorted.

def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a
