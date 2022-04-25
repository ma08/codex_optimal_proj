

def min_changes(first_str, second_str, count):
    if len(first_str) == 0 or len(second_str) == 0:
        return count
    if first_str[:1] == second_str[:1]:
        return  min_changes(first_str[1:], second_str[1:], count)
    else:
        return min_changes(first_str[1:], second_str[1:], count + 1)

def main():
    first_str = input()
    second_str = input()
    print(min_changes(first_str, second_str, 0))

if __name__ == '__main__':
    main()
