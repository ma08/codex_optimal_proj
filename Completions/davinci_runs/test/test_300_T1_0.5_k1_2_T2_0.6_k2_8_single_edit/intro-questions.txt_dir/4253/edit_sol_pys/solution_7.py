import sys
import os
import re
import shutil



def parse_file(path):
    """
    分析给定文本文件，返回其空格、制表符、行的相关信息
    :arg path: 要分析的文本文件的路径
    :return: 包含空格数、制表符数、行数的元组
    """
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    # 现在关闭打开的文件
    fd.close()

    # 以元组形式返回结果
    return spaces, tabs, i + 1

def main(path):
    """
    函数用于打印文件分析结果
    :arg path: 要分析的文本文件的路径
    :return: 若文件存在则为 True，否则 False
    """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("Spaces {}. tabs {}. lines {}".format(spaces, tabs, lines))
        return True
    else:
        return False

# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         main(sys.argv[1])
#     else:
#         sys.exit(-1)
#     sys.exit(0)


# def main():
#     r = int(sys.stdin.readline().strip())
#     print(3 * r**2)
# 
# if __name__ == '__main__':
#     main()

# def main():
#     filename = sys.argv[1]
#     infile = open(filename, 'rb')
#     outfile = open(filename + '.out', 'wb')
#     try:
#         shutil.copyfileobj(infile, outfile)
#     finally:
#         infile.close()
#         outfile.close()

# main()

# def main():
#     f = open('file.txt', 'r')
#     print(f.read())
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r')
#     print(f.readline())
#     print(f.readline())
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r')
#     for line in f:
#         print(line, end='')
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r')
#     print(f.read(16))
#     print(f.read(4))
#     print(f.read(4))
#     print(f.read())
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r')
#     print(f.read())
#     f.seek(5)
#     print(f.read())
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r+')
#     print(f.read())
#     f.write('0123456789abcdef')
#     f.seek(5)
#     print(f.read(1))
#     print(f.read(1))
#     f.seek(-3, 2)
#     print(f.read(1))
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r+')
#     f.write('0123456789abcdef')
#     f.seek(5)
#     f.write('Hello World')
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r+')
#     f.write('0123456789abcdef')
#     f.seek(5)
#     f.write('Hello World')
#     f.seek(0)
#     print(f.read())
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r+')
#     f.write('0123456789abcdef')
#     f.seek(5)
#     f.write('Hello World')
#     f.seek(0)
#     print(f.read())
#     f.seek(0)
#     f.write('XXXX')
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r+')
#     f.write('0123456789abcdef')
#     f.seek(5)
#     f.write('Hello World')
#     f.seek(0)
#     print(f.read())
#     f.seek(0)
#     f.write('XXXX')
#     f.seek(5)
#     print(f.read())
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r+')
#     f.write('0123456789abcdef')
#     f.seek(5)
#     f.write('Hello World')
#     f.seek(0)
#     print(f.read())
#     f.seek(0)
#     f.write('XXXX')
#     f.seek(5)
#     print(f.read())
#     f.seek(-4, 2)
#     f.write('YYYY')
#     f.close()
# 
# main()

# def main():
#     f = open('file.txt', 'r+')
#     f.write('0123456789abcdef')
#     f.seek(5)
#     f.write('Hello World')
#     f.seek(0)
#     print(f.read())
#     f.seek(0)
#     f.write('XXXX')
#     f.seek(5)
#     print(f.read())
#     f.seek(-4, 2)
#     f.write('YYYY')
#     f.seek(0)
#     print(f.read())
#     f.close()
# 
# main()
