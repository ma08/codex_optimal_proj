# File

## Read

```go
func ReadFile(filename string) ([]byte, error)
```

ReadFile reads the file named by filename and returns the contents.

```go
func ReadDir(dirname string) ([]os.FileInfo, error)
```

ReadDir reads the directory named by dirname and returns a list of directory entries sorted by filename.

```go
func Readlink(name string) (string, error)
```

Readlink returns the destination of the named symbolic link.

## Write

```go
func WriteFile(filename string, data []byte, perm os.FileMode) error
```

WriteFile writes data to a file named by filename.

## Copy

```go
func Copy(dst, src string) (int64, error)
```

Copy copies the contents of the file named src to the file named by dst.

## Move

```go
func Rename(oldpath, newpath string) error
```

Rename renames (moves) oldpath to newpath.

## Delete

```go
func Remove(name string) error
```

Remove removes the named file or directory.

## Stat

```go
func Stat(name string) (os.FileInfo, error)
```

Stat returns a FileInfo describing the named file.

```go
func Lstat(name string) (os.FileInfo, error)
```

Lstat returns a FileInfo describing the named file.

## Create

```go
func Create(name string) (File, error)
```

Create creates the named file with mode 0666 (before umask), truncating it if it already exists.

```go
func Mkdir(name string, perm FileMode) error
```

Mkdir creates a new directory with the specified name and permission bits.

```go
func MkdirAll(path string, perm FileMode) error
```

MkdirAll creates a directory named path, along with any necessary parents, and returns nil, or else returns an error.

```go
func Symlink(oldname, newname string) error
```

Symlink creates newname as a symbolic link to oldname.

## Open

```go
func Open(name string) (File, error)
```

Open opens the named file for reading.

```go
func OpenFile(name string, flag int, perm FileMode) (File, error)
```

OpenFile is the generalized open call; most users will use Open or Create instead.

## Temp

```go
func TempDir(dir, prefix string) (name string, err error)
```

TempDir creates a new temporary directory in the directory dir with a name beginning with prefix and returns the path of the new directory.

```go
func TempFile(dir, prefix string) (f *os.File, err error)
```

TempFile creates a new temporary file in the directory dir, opens the file for reading and writing, and returns the resulting *os.File.

## File

```go
type File struct {
    *file
}
```

A File represents an open file descriptor.

```go
func (f *File) Chdir() error
```

Chdir changes the current working directory to the file, which must be a directory.

```go
func (f *File) Chmod(mode FileMode) error
```

Chmod changes the mode of the file to mode.

```go
func (f *File) Chown(uid, gid int) error
```

Chown changes the numeric uid and gid of the named file.

```go
func (f *File) Close() error
```

Close closes the File, rendering it unusable for I/O.

```go
func (f *File) Fd() uintptr
```

Fd returns the integer Unix file descriptor referencing the open file.

```go
func (f *File) Name() string
```

Name returns the name of the file as presented to Open.

```go
func (f *File) Read(b []byte) (n int, err error)
```

Read reads up to len(b) bytes from the File.

```go
func (f *File) ReadAt(b []byte, off int64) (n int, err error)
```

ReadAt reads len(b) bytes from the File starting at byte offset off.

```go
func (f *File) Readdir(n int) ([]os.FileInfo, error)
```

Readdir reads the contents of the directory associated with file and returns a slice of up to n os.FileInfo values, as would be returned by Lstat, in directory order.

```go
func (f *File) Readdirnames(n int) (names []string, err error)
```

Readdirnames reads and returns a slice of names from the directory f.

```go
func (f *File) Seek(offset int64, whence int) (ret int64, err error)
```

Seek sets the offset for the next Read or Write on file to offset, interpreted according to whence: 0 means relative to the origin of the file, 1 means relative to the current offset, and 2 means relative to the end.

```go
func (f *File) Stat() (os.FileInfo, error)
```

Stat returns the FileInfo structure describing file.

```go
func (f *File) Sync() (err error)
```

Sync commits the current contents of the file to stable storage.

```go
func (f *File) Truncate(size int64) error
```

Truncate changes the size of the file.

```go
func (f *File) Write(b []byte) (n int, err error)
```

Write writes len(b) bytes to the File.

```go
func (f *File) WriteAt(b []byte, off int64) (n int, err error)
```

WriteAt writes len(b) bytes to the File starting at byte offset off.

```go
func (f *File) WriteString(s string) (ret int, err error)
```

WriteString is like Write, but writes the contents of string s rather than a slice of bytes.

## FileMode

```go
type FileMode uint32
```

A FileMode represents a file's mode and permission bits.

```go
const (
    // The single letters are the abbreviations
    // used by the String method's formatting.
    ModeDir        FileMode = 1 << (32 - 1 - iota) // d: is a directory
    ModeAppend                                     // a: append-only
    ModeExclusive                                  // l: exclusive use
    ModeTemporary                                  // T: temporary file; Plan 9 only
    ModeSymlink                                    // L: symbolic link
    ModeDevice                                     // D: device file
    ModeNamedPipe                                  // p: named pipe (FIFO)
    ModeSocket                                     // S: Unix domain socket
    ModeSetuid                                     // u: setuid
    ModeSetgid                                     // g: setgid
    ModeCharDevice                                 // c: Unix character device, when ModeDevice is set
    ModeSticky                                     // t: sticky)
```
