def sort_tuple(tuple_to_sort):
    if all(isinstance(x, int) for x in tuple_to_sort):
        sorted_tuple = tuple(sorted(tuple_to_sort))
        return sorted_tuple
    else:
        return tuple_to_sort