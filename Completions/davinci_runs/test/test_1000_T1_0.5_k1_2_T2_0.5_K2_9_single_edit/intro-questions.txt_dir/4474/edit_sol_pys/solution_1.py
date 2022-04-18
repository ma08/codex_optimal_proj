
#!/usr/bin/python
import os
import sys
import subprocess
 
def main():
    print("Hello World!")
    subprocess.call("ls -l", shell=True)
 
if __name__ == "__main__":
    main()
