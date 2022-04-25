The file command is a standard program on Unix-like operating systems that prints the file type of a file.
It is similar to the Unix stat command.

The file command is available on most Unix-like operating systems.
It is a standard command on the Single Unix Specification and is defined in POSIX.1-2008.

The file command was originally written by Ian F. Darwin.

For example, when run on the file /bin/ls, the file command prints:

$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.18, stripped

The file command uses the /etc/magic file to determine the file type of a file.

The file command has a number of options, including:

* -b for "brief" output, which doesn't print the file name
* -c for "checking" output, which is equivalent to the default output
* -f for "file" output, which allows the user to specify a file containing the names of files to print the file types of
* -F for "separator" output, which adds a separator between the file name and the file type
* -i for "mime" output, which prints the output in the format of a MIME Content-type
* -m for "magic" output, which allows the user to specify an alternate magic file to use
* -z for "zero" output, which prints a zero byte (ASCII NUL) after each file name instead of the usual newline

See also

* The file utility in OpenBSD

References

- file (1) (http://linux.die.net/man/1/file).
Linux Programmer's Manual.
- file (1) (http://man.cx/file(1)).
OpenBSD General Commands Manual.
- Darwin, Ian F.. file(1) (http://www.darwinsys.com/file/).
Darwin Systems.
- file (1) (http://netbsd.gw.com/cgi-bin/man-cgi?file+1+NetBSD-current).
NetBSD General Commands Manual.
- file (1) (http://www.freebsd.org/cgi/man.cgi?query=file&apropos=0&sektion=0&manpath=FreeBSD+8.1-RELEASE&arch=default&format=html).
FreeBSD General Commands Manual.
- file (1) (http://www.openbsd.org/cgi-bin/man.cgi?query=file&apropos=0&sektion=0&manpath=OpenBSD+4.8&arch=i386&format=html).
OpenBSD General Commands Manual.
- file (1) (http://www.openbsd.org/cgi-bin/man.cgi?query=file&apropos=0&sektion=0&manpath=OpenBSD+4.8&arch=amd64&format=html).
OpenBSD General Commands Manual.
- file (1) (http://www.openbsd.org/cgi-bin/man.cgi?query=file&apropos=0&sektion=0&manpath=OpenBSD+4.8&arch=sparc64&format=html).
OpenBSD General Commands Manual.
- file (http://www.opengroup.org/onlinepubs/000095399/utilities/file.html).
The Open Group Base Specifications Issue 7.
- file (1) (http://www.opengroup.org/onlinepubs/9699919799/utilities/file.html).
IEEE Std 1003.1-2008.
- file (1) (http://www.mkssoftware.com/docs/man1/file.1.asp).
MKS Toolkit for Enterprise Developers.
- file (1) (http://www.mkssoftware.com/docs/man1/file.1.asp).
MKS Toolkit for Enterprise Developers.
- file (1) (http://www.mkssoftware.com/docs/man1/file.1.asp).
MKS Toolkit for Enterprise Developers.
- file (1) (http://www.mkssoftware.com/docs/man1/file.1.asp).
MKS Toolkit for Enterprise Developers.
- file (1) (http://www.mkssoftware.com/docs/man1/file.1.asp).
MKS Toolkit for Enterprise Developers.
- file (1) (http://www.mkssoftware.com/docs/man1/file.1.asp).
MKS Toolkit for Enterprise Developers.
- file (1) (http://www.mkssoftware.com/docs/man1/file.1.asp).
MKS Toolkit for Enterprise Developers.
- file (1) (http://www.mkssoftware.com/docs/man1/file.1.asp).
MKS Toolkit for Enterprise Developers.
External links

* file (http://www.darwinsys.com/file/)
* file (http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/file.1) manual page in OpenBSD
