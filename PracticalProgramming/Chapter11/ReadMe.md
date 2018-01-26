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


    authors = set()

    for file in files:
        with open(file) as f:

            # Read first line in file

            #for line in f:

            line = f.readline()

            while line:
                if line.lower().startswith("author"):
                    author = line.split()[1].strip()
                    authors.add(author)

                line = f.readline()

    return authors
