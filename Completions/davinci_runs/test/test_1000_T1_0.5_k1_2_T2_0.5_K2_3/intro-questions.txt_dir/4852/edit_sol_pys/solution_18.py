

def main():
    expression = input()
    print(count_distinct_integers(expression))

def count_distinct_integers(expression):
    """
    Counts the number of distinct integers that can be formed from the given DPGP expression.
    :param expression: string
    :return: int
    """
    return count_distinct_integers_helper(expression, 0, len(expression), 0)

def count_distinct_integers_helper(expression, start, end, count):
    """
    Counts the number of distinct integers that can be formed from the given DPGP expression.
    :param expression: string
    :param start: int
    :param end: int
    :param count: int
    :return: int
    """
    if start == end:
        return count + 1
    if expression[start] == "+":
        return count_distinct_integers_helper(expression, start + 1, end, count) + \
               count_distinct_integers_helper(expression, start + 1, end, count)
    else:
        return count_distinct_integers_helper(expression, start + 1, end, count * 10 + int(expression[start]))

if __name__ == "__main__":
    main()
