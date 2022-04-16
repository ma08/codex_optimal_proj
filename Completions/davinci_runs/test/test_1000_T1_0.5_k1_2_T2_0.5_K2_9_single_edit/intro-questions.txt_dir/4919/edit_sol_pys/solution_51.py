import sys

def is_palindrome(s):
    s = s.lower()
    s = s.replace(' ','')
    s = s.replace('.','')
    s = s.replace(',','')
    s = s.replace('!','')
    s = s.replace('?','')
    s = s.replace('\'','')
    s = s.replace('"','')
    s = s.replace('-','')
    s = s.replace(';','')
    s = s.replace(':','')
    s = s.replace('(','')
    s = s.replace(')','')
    s = s.replace('[','')
    s = s.replace(']','')
    s = s.replace('{','')
    s = s.replace('}','')
    s = s.replace('/','')
    s = s.replace('\\','')
    s = s.replace('\n','')
    s = s.replace('\t','')
    if s == s[::-1]:
        return True
    else:
        return False

def main():
    filename = sys.argv[1]
    f = open(filename, 'r')
    print(is_palindrome(f.read()))
    f.close()

if __name__ == '__main__':
    main()
