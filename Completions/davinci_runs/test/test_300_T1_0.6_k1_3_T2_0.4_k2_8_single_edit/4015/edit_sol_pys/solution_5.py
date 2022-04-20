package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	file, err := os.Open("file.go")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	stat, err := file.Stat()
	if err != nil {
		fmt.Println(err)
		return
	}

	bs := make([]byte, stat.Size())
	_, err = file.Read(bs)
	if err != nil {
		fmt.Println(err)
		return
	}

	str := string(bs)
	fmt.Println(str)

	bs, err = ioutil.ReadFile("file.go")
	if err != nil {
		fmt.Println(err)
		return
	}
	str = string(bs)
	fmt.Println(str)
}
