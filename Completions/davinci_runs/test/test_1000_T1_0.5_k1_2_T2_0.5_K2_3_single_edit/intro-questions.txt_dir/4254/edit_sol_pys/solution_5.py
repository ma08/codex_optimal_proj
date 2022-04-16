
import sys

def main(sheep, wolves):
    if sheep < wolves:
        return "unsafe"
    else:
        return "safe"


def test_main():
    assert main(10, 5) == "safe"
    assert main(5, 10) == "unsafe"
    assert main(0, 0) == "safe"


if __name__ == '__main__':
    print(main(10, 5))
