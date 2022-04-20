import os
import sys


def main():
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.abspath(__file__))
    print(os.path.basename(os.path.abspath(__file__)))
    print(os.path.dirname(sys.argv[0]))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
    print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))))


if __name__ == "__main__":
    main()
