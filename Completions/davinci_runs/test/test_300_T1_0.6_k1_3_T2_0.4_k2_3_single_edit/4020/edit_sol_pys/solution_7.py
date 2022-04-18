
import sys

def main():
    line1 = sys.stdin.readline().strip().split(':') #split line1 by :
    line2 = sys.stdin.readline().strip().split(':') #split line2 by :
    h1 = int(line1[0])
    m1 = int(line1[1])
    h2 = int(line2[0])
    m2 = int(line2[1])

    m1 += (h1 * 60) #convert hours to minutes
    m2 += (h2 * 60)

    if m1 < m2:
        m3 = (m2 + m1) / 2 #average minutes
    else:
        m3 = (m1 + m2) / 2 + (12 * 60) #average minutes
    
    h3 = m3 / 60 #convert minutes to hours
    m3 %= 60 #get minutes
    print('{0:02d}:{1:02d}'.format(h3, m3)) #print hours and minutes

if __name__ == '__main__':
    main()
