
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <deque>
#include <sstream>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <cstring>


def main():
    S = int(input())
    print(S, ":")
    for i in range(2, S//2 + 1):
        if S % i == 0:
            j = S // i
            if i >= j:
                print("{},{}".format(i,j))

if __name__ == "__main__":
    main()
