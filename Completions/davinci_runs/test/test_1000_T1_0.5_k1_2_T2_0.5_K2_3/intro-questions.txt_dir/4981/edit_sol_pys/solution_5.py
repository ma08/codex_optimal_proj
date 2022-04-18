def main(): 
    inputs = input().strip().split() 
    inputs = [int(i) for i in inputs] 
    order = input().strip() 
    inputs = sorted(inputs) 
    for i in order: 
        print(inputs.pop(0), end=' ') 
main() 
