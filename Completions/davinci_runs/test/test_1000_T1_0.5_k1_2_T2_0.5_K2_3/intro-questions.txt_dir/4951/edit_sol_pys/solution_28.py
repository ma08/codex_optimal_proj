'''
题目描述
有一个文件，内容如下：
1. abc
2. abcde
3. abcdef
4. abcdefg
5. abcdefgh
6. abcdefghi
7. abcdefghij
8. abcdefghijk
9. abcdefghijkl
10. abcdefghijklm
其中，每行前面的数字是行号，后面的字符串是内容。请编写程序，找出其中的错误行。
错误的定义是：前面的字符串的后一个字符，在后面的字符串中找不到。
例如，第2行的内容是abcde，第3行的内容是abcdef，第3行的d在第2行中找不到，所以第3行就是错误的。
输入描述:
输入文件最多包含10行，每行格式如上述描述。
输出描述:
如果文件中存在错误行，请输出错误的行号，否则输出correct。
'''

import sys

def main():
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        lines.append(sys.stdin.readline().strip().split())
    for i in range(n):
        for j in range(i+1, n):
            if lines[j][-1] in lines[i][:-2]:  # 如果j的最后一个字符在i的除去最后两个字符的部分中
                continue  # 如果找到，跳过
            else:  # 如果没有找到，说明i的最后一个字符错误，输出i的序号
                print(i+1)
                return  # 找到后退出
    print("correct")  # 没有找到错误，输出correct

if __name__ == "__main__":
    main()
