def authors_list(files):
    authors = set()

    for file in files:
        with open(file) as f:

            # Read first line in file

            #for line in f:

            line = f.readline()

            while line:
                if line.lower().startswith("author"):
                    author = line.split()[1].strip()
                    authors.add(author)

                line = f.readline()

    return authors


#
print(authors_list(['a1.txt', 'a2.txt']))
