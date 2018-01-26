def dict_intersect(dict1, dict2):

    intersection = {}
    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            intersection[key] = value

    return intersection


print(dict_intersect({1: 2, 3: 4, 5: 7}, {1: 2, 2: 3, 3: 4}))
