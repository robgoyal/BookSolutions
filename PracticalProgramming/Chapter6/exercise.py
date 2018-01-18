def average(num_1, num_2):
    '''
    (number, number) -> number

    Return the average of num_1 and num_2.

    Examples:
        >>> average(10, 20)
        15.0
        >>> average(2.5, 3.0)
        2.75
    '''

    return (num_1 + num_2) / 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
