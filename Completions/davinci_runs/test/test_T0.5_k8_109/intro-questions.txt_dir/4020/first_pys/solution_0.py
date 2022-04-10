
def main():
    h1,m1 = [int(x) for x in input().split(':')]
    h2,m2 = [int(x) for x in input().split(':')]
    minutes = (h2*60+m2) - (h1*60+m1)
    h3 = h1 + int(minutes/120)
    m3 = m1 + (minutes/2)%60
    if m3 > 59:
        m3 = m3 - 60
        h3 = h3 + 1
    if h3 > 23:
        h3 = h3 - 24
    print('{0:02}:{1:02}'.format(int(h3),int(m3)))

main()