
import sys, re

def main():
    for line in sys.stdin:
        print re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', line),

if __name__ == '__main__':
    main() 
