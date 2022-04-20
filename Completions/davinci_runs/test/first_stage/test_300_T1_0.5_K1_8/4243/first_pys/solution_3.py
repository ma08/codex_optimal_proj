

# x = int(input())
x = 1024

# 500 yen coins
five_hundred_yen = int(x/500)

# 100 yen coins
one_hundred_yen = int((x - 500*five_hundred_yen)/100)

# 50 yen coins
fifty_yen = int((x - 500*five_hundred_yen - 100*one_hundred_yen)/50)

# 10 yen coins
ten_yen = int((x - 500*five_hundred_yen - 100*one_hundred_yen - 50*fifty_yen)/10)

# 5 yen coins
five_yen = int((x - 500*five_hundred_yen - 100*one_hundred_yen - 50*fifty_yen - 10*ten_yen)/5)

# 1 yen coins
one_yen = int((x - 500*five_hundred_yen - 100*one_hundred_yen - 50*fifty_yen - 10*ten_yen - 5*five_yen)/1)

# happiness points
happiness = 1000*five_hundred_yen + 100*one_hundred_yen + 50*fifty_yen + 10*ten_yen + 5*five_yen + 1*one_yen

print(happiness)