## Chapter 4 Solutions

#### Question 1

- ComputerScience
- Darwin's
- H2OH2OH2O
- ''

#### Question 2

- "They'll hibernate during the winter."
- "\"Absolutely not,\" he said"
- "\"He said, 'Absolutely not,'\" recalled Mel."
- "hydrogen sulfide"
- "left\right"

#### Question 3

```python
print("A\nB\nC")
```

#### Question 4

```python
print(len(''))
```

#### Question 5

```python
x = 3
y = 12.5

# Subquestion a
print("The rabbit is", x)
# Subquestion b
print("The rabbit is", x, "years old.")
# Subquestion c
print(y, "is average")
# Subquestion d
print(y, "*", x)
# Subquestion e
print(y, "*", x, "is", y*x)
```

#### Question 6

'Doe, John' is printed

#### Question 7

```python
num = float(input())
print(num)
```

#### Question 8

```python
def repeat(s, n):
    '''
    (str, int) -> str

    Return s repeated n times; if n is negative, return
    the empty string.

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    '''
    return s * n
```

### Question 9

```python
def total_length(s_1, s_2):
    '''
    (str, str) -> int

    Return the sum of the lengths of s_1 and s_2

    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    3
    >>> total_length('YES!!!!', 'Noooooo')
    14
    '''

    return len(s_1) + len(s_2)
```
