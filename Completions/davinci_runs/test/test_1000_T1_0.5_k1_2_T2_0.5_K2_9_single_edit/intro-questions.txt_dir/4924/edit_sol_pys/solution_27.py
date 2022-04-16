
def parseTime(time_str):
    h,m,s = time_str.split(":")
    return int(h), int(m), int(s)

def getTimeDiff(current_time, desired_time):
    h1,m1,s1 = parseTime(current_time)
    h2,m2,s2 = parseTime(desired_time)
    h_diff = h2 - h1
    m_diff = m2 - m1
    s_diff = s2 - s1
    if s_diff < 0:
        s_diff += 60
        m_diff -= 1
    if m_diff < 0:
        m_diff += 60
        h_diff -= 1
    if h_diff < 0:
        h_diff += 24
    return h_diff, m_diff, s_diff

def formatTime(h,m,s):
    return "{:02}:{:02}:{:02}".format(h,m,s)

def main():
    current_time = input()
    desired_time = input()
    h,m,s = getTimeDiff(current_time, desired_time)
    print(formatTime(h,m,s))

if __name__ == "__main__":
    main()
