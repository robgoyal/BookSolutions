## Chapter 5 Solutions

#### Question 1

- True
- NameError
- True
- True
- True
- True
- False
- False

#### Question 2

```python
# Subquestion a
x and y

# Subquestion b
not x

# Subquestion c
x or y
```

#### Question 3

```python
full != empty
```

#### Question 4
Yes. In the first situation, if either condition is True, we'll enter the nested if. The only way turn_camera_on() will execute is if both conditions are not True in the nested if.

The second situation will only work if both conditions are not the same. This is equivalent to the exclusive or block of code which the first fragment represents.

#### Question 5

```python
result = (abs(x) == x)
```

#### Question 6

```python
def different(a, b):
    '''
    (number, number) -> boolean

    Return True if a doesn't equal to b.

    Examples:
    >>> different(5, 10)
    True
    >>> different(1, 1)
    False
    '''

    return a != b
```

#### Question 7

```python
# Subquestion a

if population < 10000000:
    print(population)

# Subquestion b

if 10000000 <= population <= 35000000:
    print(population)

# Subquestion c

if (population / land) > 100:
    print("Densely populated")

# Subquestion d

if (population / land) > 100:
    print("Densely populated")
else:
    print("Sparsely populated")
```

#### Question 8
```python
def convert_temperatures(t, source, target):
    '''
    (number, string, string) -> float

    Converts temperature t of source units to target units.
    Source or target could be of type "Kelvin", "Celsius",
    "Fahrenheit", "Rankine", "Delisle", "Newton", "Reaumur",
    and "Romer".

    Examples:
    >>> convert_temperatures(100, "Celsius", "Fahrenheit")
    212.0
    >>> convert_temperatures(100, "Celsius", "Kelvin")
    373.15
    '''

    # Convert source to Celcius
    if source == "Fahrenheit":
        celcius = (t - 32) * 5 / 9

    elif source == "Kelvin":
        celcius = t - 273.15

    elif source == "Rankine":
        celcius = (t - 491.67) * 5 / 9

    elif source == "Delisle":
        celcius = 100 - t * 2 / 3

    elif source == "Newton":
        celcius = t * 100 / 33

    elif source == "Reaumur":
        celcius = t * 5 / 4

    elif source == "Romer":
        celcius = (t - 7.5) * 40 / 21

    elif source == "Celcius":
        celcius = t

    # Convert canonical celcius to target
    if target == "Fahrenheit":
        result = celcius * 9 / 5 + 32

    elif target == "Kelvin":
        result = celcius + 273.15

    elif target == "Rankine":
        result = (celcius + 273.15) * 9 / 5

    elif target == "Delisle":
        result = (100 - celcius) * 3 / 2

    elif target == "Newton":
        result = celcius * 33 / 100

    elif target == "Reaumur":
        result = celcius * 4 / 5

    elif target == "Romer":
        result = celcius * 21 / 40 + 7.5

    elif target == "Celcius":
        result = celcius
    return result
```

#### Question 9

The issue is that the two conditional statements are both true if ph < 3.0. Since the first condition prints out the ph, the second condition will never evaluate and print out the warning message. We could swap the order of the statements so that the warning message is displayed if the ph is less than 3.0.

#### Question 10.

- It's acidic!
- It's acidic!
- Change elif to if

#### Question 11

```python
young = age < 45
heavy = bmi >= 22.0

if young and not heavy:
    risk = 'low'
elif young and heavy:
    risk = 'medium'
elif not young and not heavy:
    risk = 'medium'
else:
    risk = 'high'
```
