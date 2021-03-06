def unique_letters(word_list):
    '''
    (list: str) -> list: char

    Return a list containing unique characters from all
    words in word_list.

    >>> unique_letters(['cat', 'dog', 'rabbit'])
    ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
    '''

    # Set removes duplicate elements created from list comprehension
    letters = list(set([letter for word in word_list for letter in word]))

    return letters
