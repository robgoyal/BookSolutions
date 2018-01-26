def count_duplicates(dictionary):
    '''
    (dict) -> int

    Return the number of values which appear
    two or more times in dictionary.

    >>> count_duplicates({'apples': 2, 'oranges': 3, 'bananas': 2, 'fruits': 3, 'kiwi': 1}
    2
    '''

    value_freq = {}
    value_two_count = 0

    for key, val in dictionary.items():
        value_freq[val] = value_freq.get(val, 0) + 1

    for val in value_freq.values():
        if val >= 2:
            value_two_count += 1

    return value_two_count


print(count_duplicates({1: 1, 2: 1, 5: 2, 3: 3, 4: 2, 7: 2}))
print(count_duplicates({}))
