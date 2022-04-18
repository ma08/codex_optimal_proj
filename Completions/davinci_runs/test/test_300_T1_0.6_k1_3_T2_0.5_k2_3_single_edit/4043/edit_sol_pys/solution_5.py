package file

import (
	"os"
)

type File struct {
	FilePath string
	FileName string
	File     *os.File
}

func NewFile(filePath string, fileName string) (*File, error) {
	file, err := os.OpenFile(filePath+"/"+fileName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0755)
	if err != nil {
		return nil, err
	}
	return &File{
		FilePath: filePath,
		FileName: fileName,
		File:     file,
	}, nil
}

func (f *File) Write(data []byte) {
	f.File.Write(data)
}

func (f *File) Close() {
	f.File.Close()
}
