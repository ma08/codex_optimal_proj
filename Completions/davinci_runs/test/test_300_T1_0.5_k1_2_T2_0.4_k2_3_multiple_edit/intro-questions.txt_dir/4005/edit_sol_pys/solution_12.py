package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	fmt.Println("Hello World")
	fmt.Println(os.Args[0])
	//fmt.Println(os.Args[1])
	//copyFile(os.Args[1], os.Args[2])
}

func copyFile(src, dst string) (w int64, err error) {
	srcFile, err := os.Open(src)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	defer srcFile.Close()

	dstFile, err := os.Create(dst)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	defer dstFile.Close()

	return io.Copy(dstFile, srcFile)
}
