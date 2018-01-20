## Chapter 8 Solutions

#### Question 1

```python
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

# Subquestion a
kingdoms[0]

# Subquestion b
kingdoms[5]

# Subquestion c
kingdoms[0:3]

# Subquestion d
kingdoms[2:5]

# Subquestion e
kingdoms[4:6]

# Subquestion f
kingdoms[0:0]
```

#### Question 2

```python
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

# Subquestion a
kingdoms[-6]

# Subquestion b
kingdoms[-1]

# Subquestion c
kingdoms[-6:-3]

# Subquestion d
kingdoms[-4:-1]

# Subquestion e
kingdoms[-2:]

# Subquestion f
kingdoms[-1:-1]
```

#### Question 3

```python
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']

# Subquestion a
appointments.append('16:30')

# Subquestion b
appointments += ['16:30']

# Subquestion c
# Append modified the original list and concactenation created a new list
```

#### Question 4

```python
ids = [4353, 2314, 2956, 3382, 9362, 3900]

# Subquestion a
del ids[3]

# Subquestion b
ids.index(9362)

# Subquestion c
ids.insert(ids.index(9362) + 1, 4499)

# Subquestion d
ids.extend([5566, 1830])

# Subquestion e
ids.reverse()

# Subquestion f
ids.sort()
```

#### Question 5

```python
# Subquestion a
alkaline_earth_metals = [4, 12, 20, 38, 56, 88]

# Subquestion b
alkaline_earth_metals[5]
alkaline_earth_metals[-1]

# Subquestion c
len(alkaline_earth_metals)

# Subquestion d
max(alkaline_earth_metals)
```

#### Question 6

```python
# Subquestion a
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]

# Subquestion b
temps.sort()

# Subquestion c
cool_temps = temps[0:2]
warm_temps = temps[2:]

# Subquestion d
temps_in_celsius = cool_temps + warm_temps
```

#### Question 7

```python
def same_first_last(L):
    '''
    (list) -> bool

    Precondition: len(L) >= 2

    Return True iff first item of the list is
    the same as the last

    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0, 4.5])
    False
    '''

    return L[0] == L[-1]
```

#### Question 8

```python
def is_longer(L1, L2):
    '''
    (list, list) -> bool

    Return True iff the length of L1 is longer than the
    length of L2.

    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    False
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
    False
    '''

    return len(L1) > len(L2)
```

#### Question 9

```python
values = [0, 1, 2]
values[1] = values
```

This creates a cyclic reference where values[1] always points to the list values.

#### Question 10

```python
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

# Subquestion a
units[0]

# Subquestion b
units[1]

# Subquestion c
units[0][0]

# Subquestion d
units[1][0]

# Subquestion e
units[0][1:]

# Subquestion f
units[1][0:2]
```

#### Question 11

```python
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

# Subquestion a
units[-2]

# Subquestion b
units[-1]

# Subquestion c
units[-2][-3]

# Subquestion d
units[-1][-3]

# Subquestion e
units[-2][-2:]

# Subquestion f
units[-1][-3:-1]
```
