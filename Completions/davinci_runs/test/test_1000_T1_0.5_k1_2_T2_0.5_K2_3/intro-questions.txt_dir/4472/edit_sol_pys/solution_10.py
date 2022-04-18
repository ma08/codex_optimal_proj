package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	fmt.Println("Hello, playground")
	data, err := ioutil.ReadFile("/Users/yuxianming/Desktop/go/src/go-study/file/file.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(string(data))
}
