## Chapter 7 Solutions

#### Question 1

- HELLO
- happy birthday!
- wEEEeeeeEEEeeeeEEE
- True
- 1
- True
- False
- Hello Python
- Hello Python! Hello World!

#### Question 2

```python
'tomato'.count('o')
```

#### Question 3

```python
'tomato'.find('o')
```

#### Question 4

```python
'tomato'.find('o', 'tomato'.find('o') + 1)
```

#### Question 5

```python
'avocado'.find('o', 'avocado'.find('o') + 1)
```

#### Question 7

```python
'runner'.replace('n', 'b')
```

#### Question 8

- `fruit.count('p')` -> `fruit.find('p', 3)` -> 5
- `fruit.upper()` -> `'PINEAPPLE'.swapcase()` -> `fruit.count('pineapple')` -> 1
- `fruit.swapcase()` -> `fruit.lower()` -> `fruit.replace("PINEAPPLE", 'pineapple')`

#### Question 9

```python
season = 'summer'
"I love {}".format(season)
```

#### Question 10

```python
side1 = 3
side2 = 4
side3 = 5

"The sides have lengths {}, {} and {}.".format(side1, side2, side3)
```

#### Question 11

```python
# Subquestion a
'boolean'.capitalize()

# Subquestion b
'CO2 H2O'.find('2')

# Subquestion c
'CO2 H2O'.find('2', 'CO2 H2O'.find('2') + 1)

# Subquestion d
'Boolean'[0].islower()

# Subquestion e
'MoNDaY'.lower().capitalize()

# Subquestion f
"  Monday".lstrip()
```

#### Question 12

```python
def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int

    Precondition: len(ch) == 1

    Return the total number of times that ch occurs in s1 and s2.

    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    >>> total_occurrences('green', 'purple', 'b')
    """

    return s1.count(ch) + s2.count(ch)
```

