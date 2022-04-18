---
title: "file"
date: 2019-03-05T15:27:49+08:00
draft: false
---


# file

## 概述

file 命令是用来检查文件类型的，它是通过检查文件的前几个字节来判断文件类型的。



## 常用参数

```
-b  去除文件名前面的路径，只输出文件名
-c  根据magic文件生成一个cache文件
-f  指定一个文件列表，file将会检查这个文件列表里面列出的文件
-F  分隔符，缺省的分隔符是“:”，-F指定分隔符
-h  如果文件是一个软连接，那么显示连接文件的文件名，而不是连接目标的文件名
-i  显示mime类型
-m  指定magic文件
-z  如果文件是压缩文件，则显示其中的文件类型
```



## 常用用法

```
file -i filename  显示文件mime类型
file -b filename  去除文件名前面的路径，只输出文件名
file -z filename  如果文件是压缩文件，则显示其中的文件类型
```



## 参考资料

[Linux file命令用法详解](https://www.cnblogs.com/ggjucheng/archive/2013/01/13/2858470.html)

[Linux file命令详解](https://www.cnblogs.com/ggjucheng/archive/2013/01/13/2858470.html)
