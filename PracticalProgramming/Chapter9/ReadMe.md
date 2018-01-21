## Chapter 9 Solutions

#### Question 1

```python
for celegans_phenotype in celegans_phenotypes:
    print(celegans_phenotype)
```

#### Question 2

```python
for half_life in half_lives:
    print(half_life, end=" ")
```

#### Question 3

```python
more_whales = whales[:]

for i in range(len(more_whales)):
    more_whales[i] += 1
```

#### Question 4

```python
# Subquestion a
alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078],
    [38, 87.62], [56, 137.327], [88, 226]]

# Subquestion b
for metal in alkaline_earth_metals:
    print(metal[0], metal[1])

# Subquestion c
number_and_weight = []

for metal in alkaline_earth_metals:
    number_and_weight.extend(metal)
```

#### Question 5

```python
def mystery_function(values):
    '''
    (list) -> list

    Returns a copy of values with each sublist
    in values reversed.

    >>> mystery_function([[1, 2, 3], [4, 5, 6]])
    [[3, 2, 1], [6, 5, 4]]
    '''

    result = []
    for sublist in values:

        # Append list to result with first value of sublist
        result.append([sublist[0]])

        # Insert each element of sublist to front of result[-1]
        for i in sublist[1:]:
            result[-1].insert(0, i)
```

#### Question 6

```python
text = ""
while text.lower() != "quit":
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("...exiting program")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")
```

#### Question 7

```python
total = 0
for population in country_populations:
    total += population
```

#### Question 8

```python
# Subquestion a

if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1")
else:
    print("Rat 1 weighed less than rat 2 on day 1")

# Subquestion b

if (rat_1[0] > rat_2[0]) and (rat_1[-1] > rat_2[-1]):
    print("Rat 1 remained heavier than Rat 2")
else:
    print("Rat 2 became heavier than Rat 1")

# Subquestion c
if (rat_1[0] > rat_2[0]):
    if (rat_1[-1] > rat_2[-1]):
        print("Rat 1 remained heavier than Rat 2")
    else:
        print("Rat 2 became heavier than Rat 1")
else:
    print("Rat 2 became heavier than Rat 1")
```

#### Question 9

```python
for i in range(33, 50):
    print(i)
```

#### Question 10

```python
for i in range(10, 0, -1):
    print(i, end=" ")
```

#### Question 11

```python
total = 0
count = 0

for i in range(2, 23):
    total += i
    count += 1

print(total / count)
```

#### Question 12

```python

def remove_neg(num_list):
    '''
    (list of number) -> list

    Remove negative numbers from the list num_list and
    returns a new list

    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    [1, 2]
    '''

    copy_list = []

    for item in num_list:
        if item > 0:
            copy_list.append(item)
```

#### Question 13

```python
for i in range(1, 8):
    print('T' * i)
```

#### Question 14

```python
for i in range(1, 8):
    print(' ' * (7 - i) + 'T' * i)
```

#### Question 15

```python
# Question 13 but with a while loop
index = 1
while (index < 8):
    print('T' * index)
    index += 1

# Question 14 but with a while loop
index = 1
while(index < 8):
    print(' ' * (7 - index) + 'T' * index)
    index += 1
```

#### Question 16

```python
# Subquestion a
weeks = 0
while (rat_1_weight < 1.25 * rat_1_weight):
    rat_1_weight += rat_1_rate * rat_1_weight
    weeks += 1

# Subquestion b
weeks = 0
while rat_1_weight < 1.1 * rat_2_weight:
    rat_1_weight += rat_1_rate * rat_1_weight
    rat_2_weight += rat_2_rate * rat_2_weight
    weeks += 1
```
