

def main():
    pass_string, message_string = 'abc', 'abcabcd'
    pass_index = 0
    for char in message_string:
        if char == pass_string[pass_index]:
            pass_index += 1
        if pass_index == len(pass_string):
            print('PASS')
            return
    print('FAIL')

if __name__ == "__main__":
    main()
