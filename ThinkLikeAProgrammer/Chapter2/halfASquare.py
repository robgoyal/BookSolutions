# Name: halfASquare
# Author: Robin Goyal
# Last-Modified: December 7, 2017
# Purpose: Print half of a square (5x5) using #'s
# Example:  #####
#           ####
#           ###
#           ##
#           #


def halfASquare():
    '''
    print half a 5x5 square using #'s
    '''

    for i in range(5, 0, -1):
        print("#" * i)


def main():
    halfASquare()


if __name__ == "__main__":
    main()
