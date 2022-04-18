

def main():
    expression = input()
    print(count_distinct_integers(expression))

def count_distinct_integers(expression):
    """
    Counts the number of distinct integers that can be formed from the given DPG expression. 
    :param expression: string
    :return: int
    """
    # There are 2^(n-1) possible ways of interpreting the pluses in the expression, where n is the number
    # of pluses. For each of these possible ways, the expression can be evaluated to a single integer, which we count.
    return count_distinct_integers_helper(expression, 0, len(expression), 0)

def count_distinct_integers_helper(expression, start, end, count):
    """
    Counts the number of distinct integers that can be formed from the given DPG expression.
    :param expression: string
    :param start: int
    :param end: int
    :param count: int
    :return: int
    """
    # Base case: We've reached the end of the expression.
    if start == end:
        return count + 1
    # Recursive case: We've reached a plus symbol.
    if expression[start] == "+":
        # We can either add or concatenate, so we call the helper function twice.
        return count_distinct_integers_helper(expression, start + 1, end, count) + \
               count_distinct_integers_helper(expression, start + 1, end, count)
    # Recursive case: We've reached a digit.
    else:
        # We concatenate the digit to the integer formed so far.
        return count_distinct_integers_helper(expression, start + 1, end, count * 10 + int(expression[start]))

if __name__ == "__main__":
    main()
