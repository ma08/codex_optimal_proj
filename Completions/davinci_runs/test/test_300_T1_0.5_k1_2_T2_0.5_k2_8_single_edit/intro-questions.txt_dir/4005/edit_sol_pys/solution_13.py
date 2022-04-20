package file

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
	"strings"
)

// File is a wrapper around os.File
type File struct {
	*os.File
}

// Open opens a file
func Open(name string) (*File, error) {
	f, err := os.Open(name)
	if err != nil {
		return nil, err
	}
	return &File{f}, nil
}

// Create creates a file
func Create(name string) (*File, error) {
	f, err := os.Create(name)
	if err != nil {
		return nil, err
	}
	return &File{f}, nil
}

// MustOpen opens a file and panics if error
func MustOpen(name string) *File {
	f, err := Open(name)
	if err != nil {
		panic(err)
	}
	return f
}

// MustCreate creates a file and panics if error
func MustCreate(name string) *File {
	f, err := Create(name)
	if err != nil {
		panic(err)
	}
	return f
}

// ReadAll reads all the content of the file
func (f *File) ReadAll() ([]byte, error) {
	b := new(bytes.Buffer)
	_, err := io.Copy(b, f)
	if err != nil {
		return nil, err
	}
	return b.Bytes(), nil
}

// ReadLines reads all the lines of the file and returns an array of strings
func (f *File) ReadLines() ([]string, error) {
	var lines []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return lines, nil
}

// WriteLines writes an array of lines to the file
func (f *File) WriteLines(lines []string) error {
	for _, line := range lines {
		_, err := f.WriteString(line)
		if err != nil {
			return err
		}
	}
	return nil
}

// Replace replaces all occurrences of old with new in the file
func (f *File) Replace(old, new string) error {
	lines, err := f.ReadLines()
	if err != nil {
		return err
	}
	for i := range lines {
		lines[i] = strings.Replace(lines[i], old, new, -1)
	}
	err = f.Truncate(0)
	if err != nil {
		return err
	}
	_, err = f.Seek(0, 0)
	if err != nil {
		return err
	}
	return f.WriteLines(lines)
}

// ReplaceInPlace replaces all occurrences of old with new in the file
func (f *File) ReplaceInPlace(old, new string) error {
	err := f.Replace(old, new)
	if err != nil {
		return err
	}
	return f.Sync()
}

// ReplaceInPlaceLines replaces all occurrences of old with new in the file
// and returns the lines read
func (f *File) ReplaceInPlaceLines(old, new string) ([]string, error) {
	lines, err := f.ReadLines()
	if err != nil {
		return nil, err
	}
	err = f.ReplaceInPlace(old, new)
	if err != nil {
		return nil, err
	}
	return lines, nil
}

// ReplaceInPlaceLinesFunc replaces all occurrences of old with new in the file
// and returns the lines read
func (f *File) ReplaceInPlaceLinesFunc(old, new string, fn func(string) error) ([]string, error) {
	lines, err := f.ReadLines()
	if err != nil {
		return nil, err
	}
	err = f.ReplaceInPlace(old, new)
	if err != nil {
		return nil, err
	}
	for _, line := range lines {
		err = fn(line)
		if err != nil {
			return nil, err
		}
	}
	return lines, nil
}

// ReplaceInPlaceFunc replaces all occurrences of old with new in the file
// and returns the lines read
func (f *File) ReplaceInPlaceFunc(old, new string, fn func(string) error) error {
	lines, err := f.ReadLines()
	if err != nil {
		return err
	}
	err = f.ReplaceInPlace(old, new)
	if err != nil {
		return err
	}
	for _, line := range lines {
		err = fn(line)
		if err != nil {
			return err
		}
	}
	return nil
}

// ReplaceFunc replaces all occurrences of old with new in the file
func (f *File) ReplaceFunc(old, new string, fn func(string) error) error {
	lines, err := f.ReadLines()
	if err != nil {
		return err
	}
	err = f.Replace(old, new)
	if err != nil {
		return err
	}
	for _, line := range lines {
		err = fn(line)
		if err != nil {
			return err
		}
	}
	return nil
}

// ReplaceLines replaces all occurrences of old with new in the file and returns the lines read
func (f *File) ReplaceLines(old, new string) ([]string, error) {
	lines, err := f.ReadLines()
	if err != nil {
		return nil, err
	}
	err = f.Replace(old, new)
	if err != nil {
		return nil, err
	}
	return lines, nil
}

// ReplaceLinesFunc replaces all occurrences of old with new in the file and returns the lines read
func (f *File) ReplaceLinesFunc(old, new string, fn func(string) error) ([]string, error) {
	lines, err := f.ReadLines()
	if err != nil {
		return nil, err
	}
	err = f.Replace(old, new)
	if err != nil {
		return nil, err
	}
	for _, line := range lines {
		err = fn(line)
		if err != nil {
			return nil, err
		}
	}
	return lines, nil
}

// ReplaceLinesFunc replaces all occurrences of old with new in the file and returns the lines read
func ReplaceLinesFunc(name, old, new string, fn func(string) error) ([]string, error) {
	f, err := Open(name)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	return f.ReplaceLinesFunc(old, new, fn)
}

// ReplaceLines replaces all occurrences of old with new in the file and returns the lines read
func ReplaceLines(name, old, new
