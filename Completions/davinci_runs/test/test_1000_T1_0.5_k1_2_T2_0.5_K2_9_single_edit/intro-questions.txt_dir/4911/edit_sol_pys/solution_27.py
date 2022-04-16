

def main():
    """main"""
    attr = input().split() # รับค่าตัวแปร
    m = int(input()) # รับค่าตัวแปร
    songs = [] # สร้างตัวแปรชื่อ songs
    for _ in range(m): # วนลูปตามตัวแปร m
        songs.append(input().split()) # เพิ่มค่าใน songs
    n = int(input()) # รับค่าตัวแปร
    for _ in range(n): # วนลูปตามตัวแปร n
        attr_sort = input() # รับค่าตัวแปร
        attr_sort_in = attr.index(attr_sort) # นับจำนวนค่าใน attr
        songs.sort(key=lambda x: x[attr_sort_in]) # เรียงค่าใน songs
        print(*attr) # แสดงค่าใน attr
        for song in songs: # วนลูปตาม songs
            print(*song) # แสดงค่าใน songs
        print() # แสดงค่า

main()
