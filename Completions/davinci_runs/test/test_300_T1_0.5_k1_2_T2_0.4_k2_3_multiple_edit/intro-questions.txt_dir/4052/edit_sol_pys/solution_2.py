package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	//reading file
	data, err := ioutil.ReadFile("test.txt") // returns byte slice
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
	fmt.Println(string(data))

	//writing file
	file, err := os.Create("test_write.txt")
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
	defer file.Close()

	file.WriteString("This is some random text\n")
}
