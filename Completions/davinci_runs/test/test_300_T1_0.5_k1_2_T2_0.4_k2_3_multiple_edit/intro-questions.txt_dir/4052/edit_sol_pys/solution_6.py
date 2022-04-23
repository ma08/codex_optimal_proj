package file

import "io/ioutil"

//ReadFile reads a file and returns the contents as a string
func ReadFile(filePath string) (string, error) {
	data, err := ioutil.ReadFile(filePath)
	return string(data), err
}

//WriteFile writes a string to a file
func WriteFile(filePath string, data string) error {
	return ioutil.WriteFile(filePath, []byte(data), 0644)
}
