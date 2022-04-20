
# Read input
N = int(input())

# Calculate the number of 1000-yen bills required
num_1000_yen_bills = N // 1000 # integer division

# Calculate the change
change = N % 1000 # modulo operation

# Print the change
print(change)
