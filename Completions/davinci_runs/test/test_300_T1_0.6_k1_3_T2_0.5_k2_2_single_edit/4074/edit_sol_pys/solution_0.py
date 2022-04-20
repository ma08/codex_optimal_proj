
def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    roman_to_int_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i in range(len(s)):
        current_value = roman_to_int_map[s[i]]
        if i == len(s) - 1:
            total += current_value
            continue
        next_value = roman_to_int_map[s[i+1]]
        if current_value < next_value:
            total -= current_value
        else:
            total += current_value
    return total
