
def main():
    k = int(input())
    desks = [int(input()) for i in range(k)]
    current_desk = 1
    passes = 0
    while any(desk > current_desk for desk in desks): # any([True, False, True]) == True
        current_desk = max(desk for desk in desks if desk <= current_desk) # максимальное значение из списка, не превышающее current_desk
        passes += 1
    print(passes)

if __name__ == '__main__':
    main()
