## Chapter 15 Questions

#### Question 2

```python
# No interesection
# [[5, 0], [5, 5]] and [[6, 0], [6, 5]] --> None

# Coincident lines
# [[0, 0], [10, 0]] and [[0, 0], [5, 0]] --> [[0, 0], [10, 0]]

# Intersection
# [[0, 0], [1, 3]] and [[3, 0], [1, 2]] --> [0.75, 2.25]

# Parallel Lines
# [[0, 0], [2, 0]] and [[0, 2], [2, 2] -> None

# No distinct points
# [[0, 0], [0, 0]] and [[5, 2], [5, 5]] -> None

# No distinct points
# [[2, 5], [3, 2]] and [[0, 0], [0, 0]] -> None
```

#### Question 5

This code will produce an error since comparisons between integers and None isn't possible.

Change the lines where min and max is initialized to the first element in the list instead.
