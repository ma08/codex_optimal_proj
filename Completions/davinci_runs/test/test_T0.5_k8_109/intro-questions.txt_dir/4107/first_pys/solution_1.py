

def main():
    n, k = map(int, input().split())
    s = input()
    router_array = []
    router_cost = 0
    direct_cost = 0
    for i in range(n):
        if s[i] == '1':
            router_array.append(i)
        else:
            direct_cost += i+1
    router_array.append(n)
    router_array.insert(0, 0)
    for i in range(len(router_array)-1):
        router_cost += (router_array[i+1] - router_array[i]) * (router_array[i+1] - router_array[i] + 1) // 2
    print(router_cost + direct_cost)

if __name__ == '__main__':
    main()