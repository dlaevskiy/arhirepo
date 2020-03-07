REGEX_PATTERN = r"([abc])([+-]?)=([abc]?)([+-]?\d*)"


def calculate(data, findall):
    matches = findall(REGEX_PATTERN)

    # var1, [sign]=, [var2], [[+-]number]
    for var1, sign, var2, number in matches:
        right = data.get(var2, 0) + int(number or 0)
        if sign == '+':
            data[var1] += right
        elif sign == '-':
            data[var1] -= right
        else:
            data[var1] = right
    return data
