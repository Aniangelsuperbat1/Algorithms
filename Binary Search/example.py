
# Binary search: Searches through a data set by seeing if the element you need is higher or lower. If Higher or lower, half of elements in set dont need to be searched, repeat process.

# O(logn)

def binary_search(sequence, item):
    start_index = 0
    end_index = len(sequence) - 1

    while start_index <= end_index:
        midpoint = start_index + (end_index - start_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
