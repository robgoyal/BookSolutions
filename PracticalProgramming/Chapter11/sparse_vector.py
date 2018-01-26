def sparse_add(vector1, vector2):

    keys = set(vector1).union(set(vector2))

    result = {}

    for key in keys:
        if key in vector1 and key in vector2:
            result[key] = vector1[key] + vector2[key]
        elif key in vector1:
            result[key] = vector1[key]
        else:
            result[key] = vector2[key]

    return result


def sparse_dot(vector1, vector2):

    dot_product = 0
    keys = set(vector1).intersection(set(vector2))

    for key in keys:
        dot_product += vector1[key] * vector2[key]

    return dot_product


print(sparse_add({0: 1, 6: 3}, {0: 3, 2: 4, 6: 2}))
