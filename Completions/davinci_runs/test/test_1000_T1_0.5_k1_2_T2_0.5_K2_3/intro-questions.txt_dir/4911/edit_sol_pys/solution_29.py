
import sys

def main():
    attributes = sys.stdin.readline().rstrip().split() # 속성들을 입력받는다.
    songs = []
    for i in range(int(sys.stdin.readline())): # 속성들의 개수만큼 반복한다.
        songs.append(sys.stdin.readline().rstrip().split()) # 입력받은 노래들의 속성들을 공백으로 분리하여 songs 리스트에 저장한다.
    for i in range(int(sys.stdin.readline())): # 정렬할 속성의 개수만큼 반복한다.
        attribute = sys.stdin.readline().rstrip() # 정렬할 속성을 입력받는다.
        songs.sort(key=lambda x: x[attributes.index(attribute)]) # 속성을 기준으로 songs 리스트를 정렬한다.
        print(' '.join(attributes)) # 속성들을 출력한다.
        for song in songs:
            print(' '.join(song)) # 정렬된 노래들의 속성들을 출력한다.
        print() # 구분을 위해 빈 줄을 출력한다.

main()
