
import sys,os

def main():
    print(os.path.abspath("file.py")) #获取文件的绝对路径
    print(os.path.exists("file.py")) #判断文件是否存在
    print(os.path.isdir("file.py")) #判断是否是目录
    print(os.path.isfile("file.py")) #判断是否是文件
    print(os.path.getsize("file.py")) #获取文件大小
    print(os.path.split("file.py")) #分割文件名与路径
    print(os.path.splitext("file.py")) #分割文件名与扩展名
    print(os.path.join("/home/peng","file.py")) #将目录和文件名合成一个路径

if __name__ == "__main__":
    main()
