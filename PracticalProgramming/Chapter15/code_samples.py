def double_preceding(values):

    if values != []:
        temp = values[0]
        values[0] = 0

        for i in range(1, len(values)):
            double = 2 * temp
            temp = values[i]
            values[i] = double


def average(values):
    count, total = 0, 0

    for value in values:
        if value is not None:
            total += value
            count += 1

    if count == 0:
        return total

    return total / count
