def db_headings(scientists):

    author_keys = set()

    for scientist in scientists:
        author_keys.update(scientists[scientist].keys())

    return author_keys


test = {
    'a': {
        1: 1,
        2: 3,
        4: 5
    },

    'b': {
        3: 2,
        2: 4,
        1: 5
    },

    'c': {
        4: 3,
        7: 9
    }
}

print(db_headings(test))
