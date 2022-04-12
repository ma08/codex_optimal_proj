
import os
import sys


def print_usage():
    print("Usage: python3 file.py [OPTION]... [FILE]...")
    print("List information about the FILEs (the current directory by default).")
    print("")
    print("  -a, --all              do not ignore entries starting with .")
    print("  -l                     use a long listing format")
    print("  -h, --human-readable   with -l, print sizes in human readable format (e.g., 1K 234M 2G)")
    print("  -r, --reverse          reverse order while sorting")
    print("  -S                     sort by file size")
    print("  -t                     sort by modification time")
    print("  -u                     with -lt: sort by, and show, access time")
    print("  -U                     do not sort; list entries in directory order")
    print("")
    print("      --help     display this help and exit")
    print("      --version  output version information and exit")


def print_version():
    print("file.py v0.1")


def parse_args(argv):
    args = {
        'all': False,
        'long': False,
        'human_readable': False,
        'reverse': False,
        'size': False,
        'time': False,
        'access_time': False,
        'directory_order': False,
        'files': []
    }

    i = 1
    while i < len(argv):
        arg = argv[i]
        if arg == '-a' or arg == '--all':
            args['all'] = True
        elif arg == '-l':
            args['long'] = True
        elif arg == '-h' or arg == '--human-readable':
            args['human_readable'] = True
        elif arg == '-r' or arg == '--reverse':
            args['reverse'] = True
        elif arg == '-S':
            args['size'] = True
        elif arg == '-t':
            args['time'] = True
        elif arg == '-u':
            args['access_time'] = True
        elif arg == '-U':
            args['directory_order'] = True
        elif arg == '--help':
            print_usage()
            sys.exit(0)
        elif arg == '--version':
            print_version()
            sys.exit(0)
        else:
            args['files'].append(arg)
        i += 1

    return args


def print_file(file, args):
    if not args['long']:
        print(file)
    else:
        print("%s %s %s %s %s %s" % (
            '-rw-r--r--',
            '1',
            'root',
            'root',
            '0',
            file
        ))


def print_files(files, args):
    for file in files:
        print_file(file, args)


def get_files(args):
    if len(args['files']) == 0:
        return os.listdir()
    else:
        files = []
        for file in args['files']:
            if os.path.isdir(file):
                files += os.listdir(file)
            else:
                files.append(file)
        return files


def main():
    args = parse_args(sys.argv)
    files = get_files(args)
    print_files(files, args)


if __name__ == '__main__':
    main()
