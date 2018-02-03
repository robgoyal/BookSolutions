## Chapter 13 Questions

#### Question 1

```python
# Version 1
def linear_search(lst, value):
    i = len(lst) - 1

    while i!= -1 and lst[i] != value:
        i = i - 1

    if i == -1:
        return -1
    else:
        return i

# Version 2
def linear_search(lst, value):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            return i

    return -1

# Version 3
def linear_search(lst, value):
    lst.insert(0, value)

    i = len(lst) - 1

    while lst[i] != value:
        i = i - 1

    lst.pop(0)

    if i == 0:
        return -1
    else:
        return i
```

#### Question 2

Since the new linear search algorithms are starting at the end of the list, they will find any duplicate values that occur closer to the end of the list.

#### Question 3

If we're performing searches on unsorted data, our only option is to use linear search. Linear search has a runtime of O(N) so if we perform x searches on a set of data using linear search, we'll have a runtime of O(xN). Therefore, if we use linear search at least log<sub>2</sub>N of searches, we'll benefit from sorting the data.

#### Question 4

##### Selection Sort

- [1, 5, 4, 3, 7, 6, 2]
- [1, 2, 4, 3, 7, 6, 5]
- [1, 2, 3, 4, 7, 6, 5]
- [1, 2, 3, 4, 7, 6, 5]
- [1, 2, 3, 4, 5, 6, 7]
- [1, 2, 3, 4, 5, 6, 7]

##### Insertion Sort

- [6, 5, 4, 3, 7, 1, 2]
- [5, 6, 4, 3, 7, 1, 2]
- [4, 5, 6, 3, 7, 1, 2]
- [3, 4, 5, 6, 7, 1, 2]
- [3, 4, 5, 6, 7, 1, 2]
- [1, 3, 4, 5, 6, 7, 2]
- [1, 2, 3, 4, 5, 6, 7]

#### Question 5

##### Pseudocode

```python
# Loop until no swaps occur
#   Loop through list
#   Compare two elements at a time
#   Check if elements are in order
#       Swap elements if out of order
```

Algorithm previously implemented at [Github link](https://github.com/robgoyal/PersonalAlgosDS/blob/master/Algorithms/Sorting/Python/bubbleSort.py)

#### Question 6

This implement of bubble sort is essentially my implementation of insertion sort at [Github link](https://github.com/robgoyal/PersonalAlgosDS/blob/master/Algorithms/Sorting/Python/insertionSort.py)
