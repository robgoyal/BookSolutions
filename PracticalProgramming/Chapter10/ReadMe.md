## Chapter 10 Solutions

#### Question 1

Refer to backup.py for the solution to Question 1.

#### Question 2

Refer to read_metals.py for the solution to Question 2.

#### Question 3

We could use the function readlines to read the entire file into a list where element is a line of the file. The readlines() function could be used to do this. Then we could loop through the list starting at the end.

#### Question 4

```python
def process_file(reader):
    '''
    (file) -> int

    Read and process reader, which must start with a time_series header.
    Return the largest value after the header.  There may be multiple pieces
    of data on each line.
    '''

    line = time_series.skip_header(reader).strip()

    # The largest value so far is the largest on this first line of data.
    largest = find_largest(line)

    # Read the remainder of the file into a string
    remaining_file = line.read()
```

#### Question 5

```python
def skip_header(reader):
    '''
    (file) -> str

    Skip the header in reader and return the first real
    piece of data.
    '''

    # Read the description line
    line = reader.readline()

    # Find the first line which contains data
    line = reader.readline()

    while line.startswith('#') or not line.strip():
        line = reader.readline()

    return line
```

#### Question 6

```python
def smallest_value_skip(reader):
    '''
    (file open for reading) -> NoneType
    Read and process reader, which must start with a time_series header.
    Return the smallest value after the header. Skip missing values,
    which are indicated with a hyphen.
    '''

    line = time_series.skip_header(reader).strip()

    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = int(line)

    for line in reader:
        line = line.strip()

        if line == '-':
            continue
        value = int(line)
        smallest = min(smallest, value)

    return smallest
```

The previous program is easier to read and understand. The continue statement overcomplicates the code and forces users to keep track of another scenario.

#### Question 7

```python
def read_molecule(reader):
    '''
    (file open for reading) -> list or NoneType
    Read a single molecule from reader and return it, or return None to signal
    end of file.  The first item in the result is the name of the compound;
    each list contains an atom type and the X, Y, and Z coordinates of that
    atom.
    '''

    # If there isn't another line, we're at the end of the file.
    line = reader.readline()

    while line.startswith('CMNT') or line.isspace():
        line = reader.readline()

    if not line:
        return None

    # Name of the molecule: "COMPND name"
    key, name = line.split()

    # Other lines are either "END" or "ATOM num atom_type x y z"
    molecule = [name]
    line = reader.readline()

    # Parse all the atoms in the molecule.
    while not line.startswith('END'):
        key, num, atom_type, x, y, z = line.split()
        molecule.append([atom_type, x, y, z])
        line = reader.readline()
    return molecule
