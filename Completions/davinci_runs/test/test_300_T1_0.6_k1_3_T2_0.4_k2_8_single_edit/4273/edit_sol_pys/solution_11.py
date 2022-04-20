
import sys
import itertools

def main():
    N = int(sys.stdin.readline())
    names = [sys.stdin.readline().rstrip() for _ in range(N)]
    marc_names = [name for name in names if name[0] in ["M", "A", "R", "C", "H"]]
    marc_names.sort() # 文字列のソートは昇順
    # 3文字選ぶ組み合わせのうち、先頭文字が異なるものの数を求める
    print(len([c for c in itertools.combinations(marc_names, 3) if len(set(map(lambda x:x[0], c))) == 3]))

if __name__ == "__main__":
    main()
