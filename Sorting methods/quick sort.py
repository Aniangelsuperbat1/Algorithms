#Takes an unsorted sequence and sorts it either in ascending order or descending order
#Takes one item to be a "pivot" point
#pivot is just the number we use to base our comparisons of all the other numbers off of
#Two lists: Less than Pivot number and More than Pivot number
#can use any number to be the pivot point
#if list is unsorted after one round, repeat process
#worst case Senario: O(n) squared

def quick_sort(sequence):
    length = len(sequence)
    if length <=1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)