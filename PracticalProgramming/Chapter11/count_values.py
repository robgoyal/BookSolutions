def count_values(colors):
    '''
    (dict) -> int

    Return the number of unique values in the dictionary colors.

    >>> count_values({'red': 1, 'green': 1, 'blue': 2})
    2
    '''

    unique_values = set(colors.values())

    return len(unique_values)
