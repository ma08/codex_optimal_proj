

import sys

def main():
    n = int(sys.stdin.readline().strip())  # 读取行数
    lines = []
    for i in range(n):
        lines.append(sys.stdin.readline().strip().split())  # 将每行内容按空格分割后存入lines中
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
