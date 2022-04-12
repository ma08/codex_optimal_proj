
def main():
    pass_str, message_str = input().split(' ')
    pass_ind = 0
    for char in message_str:
        if char == pass_str[pass_ind]:
            pass_ind += 1
        if pass_ind == len(pass_str):
            print('PASS')
            return
    print('FAIL')


if __name__ == "__main__":
    main()
