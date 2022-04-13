

def main():
    r, D, x_2000 = map(int, input().split())
    for i in range(1, 11):
        print(r * x_2000 - D)
        x_2000 = r * x_2000 - D 
        
if __name__ == '__main__':
    main()
