

def check_harshad_number(n):
    sn = str(n)
    ssum = sum([int(x) for x in sn])
    if n % ssum == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(check_harshad_number(int(input())))
