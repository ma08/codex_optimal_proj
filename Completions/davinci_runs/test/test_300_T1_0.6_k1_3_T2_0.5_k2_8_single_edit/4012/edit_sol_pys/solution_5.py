

# test_cases = int(input())
# while test_cases > 0:
#     a, b, c = [int(x) for x in input().split()]
#     ans = 0
#     if b % a == 0 and c % b == 0:
#         print(ans)
#         print(a, b, c)
#     else:
#         a_n = 1
#         b_n = 1
#         c_n = 1
#         while a_n * b_n * c_n != 1:
#             if b % a == 0 and c % b == 0:
#                 if a_n * b_n * c_n == 1:
#                     break
#                 else:
#                     a += a_n
#                     b += b_n
#                     c += c_n
#                     ans += 1
#                     continue
#             else:
#                 if a_n == 1:
#                     a_n = -1
#                 else:
#                     a_n = 1
#                 if b_n == 1:
#                     b_n = -1
#                 else:
#                     b_n = 1
#                 if c_n == 1:
#                     c_n = -1
#                 else:
#                     c_n = 1
#                 a += a_n
#                 b += b_n
#                 c += c_n
#                 ans += 1
#         print(ans)
#         print(a, b, c)
#     test_cases -= 1

test_cases = int(input())
while test_cases > 0:
    a, b, c = [int(x) for x in input().split()]
    ans = 0
    if b % a == 0 and c % b == 0:
        print(ans)
        print(a, b, c)
    else:
        a_n = 1
        b_n = 1
        c_n = 1
        while a_n * b_n * c_n != 1:
            if b % a == 0 and c % b == 0:
                if a_n * b_n * c_n == 1:
                    break
                else:
                    a += a_n
                    b += b_n
                    c += c_n
                    ans += 1
                    continue
            else:
                if a_n == 1:
                    a_n = -1
                else:
                    a_n = 1
                if b_n == 1:
                    b_n = -1
                else:
                    b_n = 1
                if c_n == 1:
                    c_n = -1
                else:
                    c_n = 1
                a += a_n
                b += b_n
                c += c_n
                ans += 1
        print(ans)
        print(a, b, c)
    test_cases -= 1

test_cases = int(input())
while test_cases > 0:
    a, b, c = [int(x) for x in input().split()]
    ans = 0
    if b % a == 0 and c % b == 0:
        print(ans)
        print(a, b, c)
    else:
        a_n = 1
        b_n = 1
        c_n = 1
        while a_n * b_n * c_n != 1:
            if b % a == 0 and c % b == 0:
                if a_n * b_n * c_n == 1:
                    break
                else:
                    a += a_n
                    b += b_n
                    c += c_n
                    ans += 1
                    continue
            else:
                if a_n == 1:
                    a_n = -1
                else:
                    a_n = 1
                if b_n == 1:
                    b_n = -1
                else:
                    b_n = 1
                if c_n == 1:
                    c_n = -1
                else:
                    c_n = 1
                a += a_n
                b += b_n
                c += c_n
                ans += 1
        print(ans)
        print(a, b, c)
    test_cases -= 1
