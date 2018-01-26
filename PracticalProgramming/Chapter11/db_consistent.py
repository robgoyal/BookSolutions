def db_consistent(scientists):

    inner_dicts = scientists.values()

    for i in range(len(inner_dicts) - 1):
        if inner_dicts[i].keys() != inner_dicts[i + 1].keys():
            return False

    return True


test = {
    'a': {
        1: 1,
        2: 3,
        4: 5
    },

    'b': {
        1: 2,
        2: 4,
        4: 5
    },

    'c': {
        1: 3,
        2: 9,
        4: 8
    }
}

print(db_consistent(test))
