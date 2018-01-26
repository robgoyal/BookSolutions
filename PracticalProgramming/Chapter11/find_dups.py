def find_dups(data):
    '''
    (list) -> set

    Returns a set of integers which occur at least two times
    in data.

    >>> list_ints = [8, 2, 1, 3, 6, 2, 8, 1, 2]
    >>> find_dups(list_ints)
    set([8, 2, 1])
    >>> find_dups([1, 2, 3])
    set([])
    '''

    int_to_freq = {}
    elem_set = set()

    for value in data:
        int_to_freq[value] = int_to_freq.get(value, 0) + 1

    for value, count in int_to_freq.items():
        if count >= 2:
            elem_set.add(value)

    return elem_set
