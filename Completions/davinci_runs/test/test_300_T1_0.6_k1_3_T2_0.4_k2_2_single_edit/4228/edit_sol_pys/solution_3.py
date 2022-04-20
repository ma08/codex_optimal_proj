#!/usr/bin/env python
# coding: utf-8


def main():
    n,l = map(int, input().split())
    print(flavor_list)
    flavor_list = [l + i for i in range(n)]
    print(sum(flavor_list[1:]))

if __name__ == "__main__":
    main()
