# Name: backup.py
# Author: Robin Goyal
# Last-Modified: January 23, 2018
# Purpose: Create a backup of a file


def create_backup(in_file, out_file):
    '''
    (file to read, file to write) -> None

    Copy the contents of in_file to out_file.
    '''

    # Write in_file contents as string to out_file
    out_file.write(in_file.read())


if __name__ == "__main__":
    file = input("Name of file to create a backup of: ")

    with open(file, 'r') as in_file, open(file + '.bak', 'w') as out_file:
        create_backup(in_file, out_file)
