
import numpy as np


def main():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(np.sum(a, axis=0))
    print(np.sum(a, axis=1))
    print(np.sum(a, axis=0, keepdims=True))
    print(a.sum(axis=0))
    print(a.sum(axis=0, keepdims=True))


if __name__ == '__main__':
    main()
