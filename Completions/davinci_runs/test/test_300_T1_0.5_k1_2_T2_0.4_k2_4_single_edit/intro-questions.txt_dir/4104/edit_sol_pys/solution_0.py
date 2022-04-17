

def main():
    expression = input().split('+')
    print(sum(map(lambda x: sum(map(int, x.split('-'))), expression)))

main()
