def mating_pairs(males, females):

    pairs = set()
    for i in range(len(males)):
        pairs.add((males.pop(), females.pop()))

    return pairs


if __name__ == "__main__":
    print(mating_pairs({"robin", "ajay"}, {"cool", "kid"}))
