
# n = int(input())
# trips = []
# for i in range(n):
#     country, year = input().split()
#     year = int(year)
#     trips.append((country, year))

# q = int(input())
# queries = []
# for i in range(q):
#     country, k = input().split()
#     k = int(k)
#     queries.append((country, k))

# for query in queries:
#     country, k = query
#     trips_to_country = [trip for trip in trips if trip[0] == country]
#     trips_to_country.sort(key=lambda t: t[1], reverse=True)
#     print(trips_to_country[k - 1][1])


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# def fib_memoized(n):
#     memo = [0, 1]
#     if n >= len(memo):
#         for i in range(len(memo), n + 1):
#             memo.append(memo[i - 1] + memo[i - 2])
#     return memo[n]


# def fib_memoized_with_dict(n):
#     memo = {0: 0, 1: 1}
#     if n not in memo:
#         memo[n] = fib_memoized_with_dict(n - 1) + fib_memoized_with_dict(n - 2)
#     return memo[n]


# def fib_iterative(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a = 0
#         b = 1
#         for i in range(n):
#             a, b = b, a + b
#         return a


# print(fib_iterative(10))


# def fib_iterative_with_dict(n):
#     memo = {0: 0, 1: 1}
#     for i in range(2, n + 1):
#         memo[i] = memo[i - 1] + memo[i - 2]
#     return memo[n]


# print(fib_iterative_with_dict(10))


# def fib_iterative_with_list(n):
#     memo = [0, 1]
#     for i in range(2, n + 1):
#         memo.append(memo[i - 1] + memo[i - 2])
#     return memo[n]


# print(fib_iterative_with_list(10))


# def fib_iterative_with_list_and_tuple(n):
#     memo = [0, 1]
#     for i in range(2, n + 1):
#         memo.append(sum(memo[-2:]))
#     return memo[n]


# print(fib_iterative_with_list_and_tuple(10))


# def fib_iterative_with_tuple(n):
#     memo = (0, 1)
#     for i in range(2, n + 1):
#         memo = (memo[1], sum(memo))
#     return memo[1]


# print(fib_iterative_with_tuple(10))


# def fib_iterative_with_tuple_and_list(n):
#     memo = (0, 1)
#     for i in range(2, n + 1):
#         memo = (memo[1], sum(list(memo)))
#     return memo[1]


# print(fib_iterative_with_tuple_and_list(10))


# def fib_iterative_with_tuple_and_list_and_tuple(n):
#     memo = (0, 1)
#     for i in range(2, n + 1):
#         memo = (memo[1], sum(list(memo)))
#     return memo[1]


# print(fib_iterative_with_tuple_and_list_and_tuple(10))


# def fib_iterative_with_tuple_and_tuple(n):
#     memo = (0, 1)
#     for i in range(2, n + 1):
#         memo = (memo[1], sum(memo))
#     return memo[1]


# print(fib_iterative_with_tuple_and_tuple(10))


# def fib_iterative_with_tuple_and_tuple_and_list(n):
#     memo = (0, 1)
#     for i in range(2, n + 1):
#         memo = (memo[1], sum(list(memo)))
#     return memo[1]


# print(fib_iterative_with_tuple_and_tuple_and_list(10))


# def fib_iterative_with_tuple_and_tuple_and_tuple(n):
#     memo = (0, 1)
#     for i in range(2, n + 1):
#         memo = (memo[1], sum(memo))
#     return memo[1]


# print(fib_iterative_with_tuple_and_tuple_and_tuple(10))


# def fib_iterative_with_tuple_and_tuple_and_tuple_and_list(n):
#     memo = (0, 1)
#     for i in range(2, n + 1):
#         memo = (memo[1], sum(list(memo)))
#     return memo[1]


# print(fib_iterative_with_tuple_and_tuple_and_tuple_and_list(10))
