

def is_lucky(number):
    num_str = str(number)
    if len(num_str) % 2 != 0:
        return False
    first_half = num_str[0:len(num_str)//2]
    second_half = num_str[len(num_str)//2:len(num_str)]
    return sum([int(x) for x in first_half]) == sum([int(x) for x in second_half])

if __name__ == "__main__":
    print("Yes" if is_lucky(int(input())) else "No")