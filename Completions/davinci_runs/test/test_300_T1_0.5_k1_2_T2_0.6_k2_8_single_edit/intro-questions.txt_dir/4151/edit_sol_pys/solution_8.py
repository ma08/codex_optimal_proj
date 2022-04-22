

def main():
    n = int(input())
    s = list(input().split())
    t = list(input().split())
    st = []
    for i in range(n):
        if s[i] not in st and t[i] not in st:
            st.append(s[i])
            st.append(t[i])
        elif s[i] in st and t[i] not in st:
            st.remove(s[i])
            st.append(t[i])
        elif s[i] not in st and t[i] in st:
            st.remove(t[i])
            st.append(s[i])
        else:
            pass
    print(len(st))


if __name__ == "__main__":
    main()
