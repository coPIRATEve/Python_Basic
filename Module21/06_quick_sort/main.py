def partition(arr):
    pivot = arr[-1]
    less = []
    equal = []
    greater = []
    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)

    return less, equal, greater
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    less, equal, greater = partition(arr)
    sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)
    return sorted_less + equal + sorted_greater

