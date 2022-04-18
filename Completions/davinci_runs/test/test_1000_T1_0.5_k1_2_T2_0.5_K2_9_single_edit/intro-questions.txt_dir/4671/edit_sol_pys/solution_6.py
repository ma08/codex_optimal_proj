


def wrapper(func):
    def fun(l):  # complete the function
        func(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
    return fun


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]  # input list
    sort_phone = wrapper(sort_phone)
    sort_phone(l)  # sort list
