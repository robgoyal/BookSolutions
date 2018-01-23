# Name: read_metals.py
# Author: Robin Goyal
# Last-Modified: January 23, 2018
# Purpose: Read a txt file containing alkaline metals


def read_metals(file):
    '''
    (file) -> list

    Read the contents of file and return a list with each
    item being a list containing information about each metal
    (line) from file.
    '''

    result = []

    for line in file:
        result.append(line.split())

    return result


if __name__ == "__main__":
    with open('alkaline_metals.txt') as f:
        print(read_metals(f))
