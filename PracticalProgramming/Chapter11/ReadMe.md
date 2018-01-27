## Chapter 11 Solutions

#### Question 1

```python
def find_dups(data):
    '''
    (list) -> set

    Returns a set of integers which occur at least two times
    in data.

    >>> list_ints = [8, 2, 1, 3, 6, 2, 8, 1, 2]
    >>> find_dups(list_ints)
    {8, 2, 1}
    >>> find_dups([1, 2, 3])
    set([])
    '''

    int_to_freq = {}
    elem_set = set()

    for value in data:
        int_to_freq = int_to_freq.get(value, 0) + 1

    for value, count in int_to_freq.items():
        if count >= 2:
            elem_set.add(value)

    return elem_set
```

#### Question 2

```python
def mating_pairs(males, females):
    '''
    (set: str, set: str) -> set: tuple: (str, str)

    Return a set of tuples which includes a pair of
    gerbils from the male set and female set.

    >>> mating_pairs({"bob", "john"}, {"sam", "alice"})
    {("bob", "sam"), ("john", "alice")}
    '''

    pairs = set()
    for i in range(len(males)):
        pairs.add((males.pop(), females.pop()))

    return pairs
```

#### Question 3

```python
def authors_list(files):
    '''
    (list: file) -> set

    Return a set of authors found in each
    file from files.
    '''

    authors = set()

    for file in files:
        with open(file) as f:

            # Read first line in file
            line = f.readline()

            # Loop until reaching EOF
            while line:
                if line.lower().startswith("author"):
                    author = line.split()[1].strip()
                    authors.add(author)

                line = f.readline()

    return authors
```

#### Question 4

```python
def count_values(colors):
    '''
    (dict) -> int

    Return the number of unique values in the dictionary colors.

    >>> count_values({'red': 1, 'green': 1, 'blue': 2})
    2
    '''

    unique_values = set(colors.values())
    return len(unique_values)
```

#### Question 5

```python
def lowest_probability(particles):
    '''
    (dict) -> string

    Returns the particle with the lowest probably in
    the dictionary particles.

    >>> lowest_probability({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03})
    meson
    '''

    return min(particles, key=particles.get)
```

#### Question 6

```python
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

    # Populate dict with frequency of values
    for key, val in dictionary.items():
        value_freq[val] = value_freq.get(val, 0) + 1

    for val in value_freq.values():
        if val >= 2:
            value_two_count += 1

    return value_two_count
```

#### Question 7

```python
def is_balanced(rgb_dict):
    '''
    (dict) -> bool

    Return True iff the values in
    the dictionary sum to 1.0.

    >>> is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})
    True
    '''

    return sum(rgb_dict.values()) == 1
```

#### Question 8

```python
def dict_intersect(dict1, dict2):
    '''
    (dict, dict) -> dict

    Return a dictionary which contains the
    key/value pairs found in dict1 and dict2.

    >>> dict_intersect({1: 2, 3: 4, 5: 7}, {1: 2, 2: 3, 3: 4})
    {1: 2, 3: 4}
    '''

    intersection = {}
    for key, value in dict1.items():

        # Check if key and value from dict1 are same as dict2
        if key in dict2 and dict2[key] == value:
            intersection[key] = value

    return intersection
```

#### Question 9

```python
def db_headings(scientists):
    '''
    (dict) -> set

    Return a set of all keys for each
    scientist in the dictionary, scientists.
    '''

    author_keys = set()

    for scientist in scientists:
        author_keys.update(scientists[scientist].keys())

    return author_keys
```

#### Question 10

```python
def db_consistent(scientists):
    '''
    (dict) -> bool

    Return True iff each inner dictionary
    from scientists contains the same keys.
    '''

    # List containing inner dictionaries
    inner_dicts = scientists.values()

    for i in range(len(inner_dicts) - 1):

        # Compare list of keys for each inner dictionary
        if inner_dicts[i].keys() != inner_dicts[i + 1].keys():
            return False

    return True
```

#### Question 11

```python
# Subquestion a
def sparse_add(vector1, vector2):
    '''
    (dict, dict) -> dict

    Return a dictionary containing the result
    of adding vectors, vector1 and vector2.

    A sparse vector is a vector where most entries
    are zero. {0: 1, 6: 3} is equivalent to
    [1, 0, 0, 0, 0, 0, 3, 0, 0].

    >>> sparse_add({0: 1, 3: 2}, {1: 4, 3: 5})
    {0: 1, 1: 4, 3: 7}
    '''

    # Create set of all keys
    keys = set(vector1).union(set(vector2))

    result = {}

    for key in keys:
        # Sum each value if values at both positions in vectors
        if key in vector1 and key in vector2:
            result[key] = vector1[key] + vector2[key]

        # Value in one position at either vector
        elif key in vector1:
            result[key] = vector1[key]
        else:
            result[key] = vector2[key]

    return result

# Subquestion b
def sparse_dot(vector1, vector2):
    '''
    (dict, dict) -> int

    Return an integer containing the result of
    the dot product of vectors, vector1 and vector2.

    >>> sparse_dot({0: 1, 6: 3}, {0: 3, 2: 4, 6: 2})
    9
    '''

    dot_product = 0

    # Create set of same keys from both dictionaries
    keys = set(vector1).intersection(set(vector2))

    for key in keys:
        dot_product += vector1[key] * vector2[key]

    return dot_product

# Subquestion c

# We would need to ask what the end of the list would be represented by
```
