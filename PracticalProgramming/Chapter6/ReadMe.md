## Chapter 6 Solutions

#### Question 1

```python
import math

# Subquestion a
math.floor(-2.8)

# Subquestion b
abs(round(-4.3))

# Subquestion c
math.ceil(math.sin(34.5))
```

#### Question 2

```python
# Subquestion b
import calendar

# Subquestion c
help(calendar.isleap)

# Subquestion d
year = 2018
while (not calendar.isleap(year)):
    year += 1
print(year)

# Subquestion e
dir(calendar)

# Subquestion f
# leapdays is a function which returns number of leap years
# in a range
calendar.leapdays(2000, 2051)

# Subquestion g
# weekday will return the day of a certain date
calendar.weekday(2016, 7, 29)
```

#### Question 3

Solution is in a seperate file called exercise.py.
