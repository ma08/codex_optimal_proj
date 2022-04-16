
def dpg(string):
    if '+' not in string:
        return 1
    else:
        count = 0
        for i in range(len(string)):
            if string[i] == '+':
                count += dpg(string[:i]) * dpg(string[i+1:])
        return count


if __name__ == '__main__':
    print(dpg(input()))
