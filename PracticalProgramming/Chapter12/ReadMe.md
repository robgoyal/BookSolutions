## Chapter 11 Solutions

#### Question 1

```python
# Subquestion a

# Convert the string into a list to change its values
# Look at each value of the list
#   If item is T
#       Change it to A
#   Else if item is A
#       Change it to T
#   Else if item is G
#       Change it to C
#   Else
#       Change it to G
# Return the list as a string

# Subquestion b

# No, it will not return to it's original value

# Subquestion c

def complement(sequence):
    '''
    (str) -> str

    Return the complement of a DNA sequence.

    >>> complement('AATCGCATAGC')
    TTAGCGTATCG
    '''

    # Convert string of letters to list
    list_seq = list(sequence)

    # Swap each character with its complement
    for i in range(len(list_seq)):
        if list_seq[i] == 'T':
            list_seq[i] = 'A'

        elif list_seq[i] == 'A':
            list_seq[i] = 'T'

        elif list_seq[i] == 'G':
            list_seq[i] = 'C'

        else:
            list_seq[i] = 'G'

    # Return the complement as a string
    return "".join(list_seq)
```

#### Question 2

```python
# Subquestion a

# Assuming data is the list I'm looping through to look for min value and index
min_val = data[0]
min_index = 0

for i in range(1, len(data)):
    if data[i] < min_val:
        min_val = data[i]
        min_index = i

# Subquestion b
def min_index(data):
    '''
    (list) -> tuple

    Return a tuple containing the minimum
    value and index of the minimum value from data.

    >>> min_index([5, 2, 0, 1])
    (0, 2)
    '''

    return min(data), data.index(min(data))

# Subquestion c
def min_or_max_index(data, switch):
    '''
    (list, bool) -> tuple

    Returns the max value and index in data if switch
    is Flase, else it returns the minimum value and index.

    >>> min_or_max_index([4, 2, 1, 3, 5], True)
    (1, 2)
    >>> min_or_max_index([4, 2, 1, 3, 5], False)
    (5, 4)
    '''

    if switch:
        return min(data), data.index(min(data))

    return max(data), data.index(max(data))
```

#### Question 3

- Initialize variables for total and number of years
- Skip over headers until reaching data
- Loop through data
-   Add pelt for year to total
-   Increase the number of year by 1
- Return average of total pelts / total years

```python
def hopedale_average(file):
    '''
    (file) -> float

    Return the average number of pelts
    produced per year from file.
    '''

    # Read the description line
    file.readline()

    # Read comment lines until we read the first piece of data
    data = file.readline().strip()
    while data.startswith('#'):
        data = file.readline().strip()

    # Initiaize variables to calculate average
    total_pelts = int(data)
    total_years = 1

    # Read remainder of data
    for data in file:
        total_pelts += int(data.strip())
        total_years += 1

    return total_pelts / total_years
```

#### Question 4

```python
def find_two_smallest(L):
    '''
    (list) -> tuple

    Return a tuple of the indices of the two smallest
    values in list L.

    >>> find_two_smallest([1, 2])
    (0, 1)
    >>> find_two_smallest([2, 1])
    (1, 0)
    >>> find_two_smallest([4, 3, 2, 1])
    (3, 2)
    >>> find_two_smallest([1, 2, 3, 0])
    (3, 0)
    '''
```

#### Question 5

If a list with any length less than 2 is passed to the function, it would return an error. Since we're accessing the second element in the list, we would get an index error. If an empty list is passed, it should return an empty tuple. If a list of length one is passed, it should return a tuple with a single index.

#### Question 6

```python
def dutch_flag(L):
    '''
    (list) -> None

    Rearrange L so that it stores the strings in the
    order of the Dutch national flag (Red, Green, and Blue).

    >>> dutch_flag(['blue', 'green', 'red', 'red', 'blue'])
    ['red', 'red', 'green', 'blue', 'blue']
    '''

    # Sort list lexicographically in reverse order
    L.sort(reverse=True)
```
