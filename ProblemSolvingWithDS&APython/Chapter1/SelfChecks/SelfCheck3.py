# Name: SelfCheck3.py
# Author: Robin Goyal
# Last-Modified: January 30, 2018
# Purpose: Design a prorogram to determine how long it would take for Python
#          to create a string randomly from Shakespeare

from string import ascii_lowercase
import random


def create_random_string(n):
    '''
    () -> str

    Return a string of size n with each
    character a randomly chosen lowercase letter

    >>> create_random_string()
    'raukpvevtnyuwymtmzmuiyswqes'
    '''

    # Include space as a potential character
    alphabet = ascii_lowercase + ' '
    random_string = [random.choice(alphabet) for i in range(n)]

    return "".join(random_string)


def score_string(random_string, desired_string):
    '''
    (str, str) -> int

    Returns an integer representing the number
    of similar characters in random_string and
    desired_string.

    >>> score_string("aslqiqmvkx n yncfklfrfkkujh", "methinks it is like a weasel")
    0
    '''

    score = 0
    for char_1, char_2 in zip(random_string, desired_string):
        if char_1 == char_2:
            score += 1

    return score


def main():

    # Constants for this program
    DESIRED_STRING = "methinks it is like a weasel"
    DESIRED_STRING_LEN = len(DESIRED_STRING)

    best_score = 0
    best_string = ""
    runs = 0

    while True:

        # Get random string and score
        random_string = create_random_string(DESIRED_STRING_LEN)
        random_score = score_string(random_string, DESIRED_STRING)

        # Update current best with randomly generated information
        if random_score > best_score:
            best_score = random_score
            best_string = random_string

        runs += 1

        # Display current best information
        if runs % 3000 == 0:
            print("String: {} has Score: {}".format(best_string, best_score))


if __name__ == "__main__":
    main()
