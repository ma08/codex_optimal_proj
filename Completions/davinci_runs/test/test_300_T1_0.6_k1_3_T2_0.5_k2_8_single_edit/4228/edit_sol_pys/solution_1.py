
def make_flavor_list(n,l):
    return [l + i for i in range(n)]

def main():
    n,l = map(int, input().split())
    flavor_list = make_flavor_list(n,l)
    print(sum(flavor_list[1:]))

if __name__ == "__main__":
    main()
