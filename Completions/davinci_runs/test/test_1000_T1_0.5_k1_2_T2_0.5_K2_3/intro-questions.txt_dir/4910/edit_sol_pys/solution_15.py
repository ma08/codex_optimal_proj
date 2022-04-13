

def main():
    """
    This is the main function.
    """
    num_inputs = int(input())
    clothes_dict = {}
    for i in range(num_inputs):
        clothes = input()
        if clothes in clothes_dict:
            clothes_dict[clothes] += 1
        else:
            clothes_dict[clothes] = 1
    max_clothes = max(clothes_dict.values())
    for clothes in clothes_dict:
        if clothes_dict[clothes] == max_clothes:
            print(clothes)

if __name__ == "__main__":
    main()
