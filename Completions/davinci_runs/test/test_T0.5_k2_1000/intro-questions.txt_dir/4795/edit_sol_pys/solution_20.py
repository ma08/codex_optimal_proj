

# Find the number of unique characters in the string
# Find the number of unique characters in the substring
# Find the number of unique characters in the string that are not in the substring
# Find the number of unique characters in the substring that are not in the string
# Add up all of those numbers

def main():
    s = input()
    t = input()
    s_unique = len(set(s))
    t_unique = len(set(t))
    s_not_t = len(set(s) - set(t))
    t_not_s = len(set(t) - set(s))
    print(s_unique + t_unique - s_not_t - t_not_s)


main()
