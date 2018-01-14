## Chapter 3 Solutions

#### Question 1

1. min(2, 3, 4) returns 2
2. max(2, -3, 4, 7, -5) returns 7
3. max(2, -3, min(4, 7), -5) returns 4

#### Question 2

1. max(3, 4) is evaluated first, then abs(-5) is evaluted, then min(4, 5)
2. max(2, 8) then min(4, 6, 8), then abs(4)
3. max(5.572, 3.258), then abs(-2), then round(5.572, 2)

#### Question 3

```python
def triple_number(number):
    '''
    number -> number

    Returns a number tripled.

    >>> triple_number(-3)
    -9
    >>> triple_number(0)
    0
    >>> triple_number(15)
    45
    '''

    return 3 * number
```

#### Question 4

```python
def abs_diff(num_1, num_2):
    '''
    (number, number) -> number

    Returns the absolute difference between num_1 and num_2

    >>> abs_diff(1, 3):
    2
    >>> abs_diff(5, -1):
    6
    '''

    return abs(num_1 - num_2)
```

#### Question 5

```python
def km_to_miles(kilometers):
    '''
    number -> float

    Returns the number of miles in kilometers.

    >>> km_to_miles(1)
    0.625
    >>> km_to_miles(12)
    7.5
    '''
    return kilometers / 1.6
```

#### Question 6

```python
def average_grades(grade_1, grade_2, grade_3):
    '''
    (number, number, number) -> number

    Returns the average of grade_1, grade_2, and grade_3
    where each grade is between 0 and 100 inclusive.

    >>> average_grades(50, 85, 77)
    70.67
    >>> average_grades(100, 25, 68)
    64.33
    '''

    return (grade_1 + grade_2 + grade_3) / 3
```

#### Question 7

```python
def best_average_grades(grade_1, grade_2, grade_3, grade_4):
    '''
    (number, number, number, number) -> number

    Returns the best 3 grades from grade_1, grade_2, grade_3 and
    grade_4 where each grade is between 0 and 100 inclusive.

    >>> best_average_grades(50, 100, 75, 25)
    75
    '''

    return max(average_grades(grade_1, grade_2, grade_3),
               average_grades(grade_1, grade_2, grade_4)
               average_grades(grade_2, grade_3, grade_4)
               average_grades(grade_1, grade_3, grade_4))
```

#### Question 8

```python
def weeks_elapsed(day_1, day_2):
    '''
    (int, int) -> int

    Return the number of full weeks that have elapsed
    between the two days. day_1 and day_2 are in the
    same year and between 1 and 365.

    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    '''

    return abs(day_1 - day_2) // 7
```

#### Question 9

- Parameter: num
- Argument: 3
- Function name: square
- Function call: square(3)

#### Question 10

```python
def square(num):
    '''
    (number) -> number

    Return the square of num.

    >>> square(3)
    9
    '''

    return num ** 2
```
