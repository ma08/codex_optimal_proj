
# === import ======================================================================================================================================================
import sys
#
# === const =======================================================================================================================================================

# === functions ===================================================================================================================================================

# === classes =====================================================================================================================================================

# === main ========================================================================================================================================================
def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    dif = [abs(t - h[i] * 0.006 - a) for i in range(n)]
    ans = dif.index(min(dif)) + 1
    print(ans)

# =====================================================================================================================================================================
if __name__ == "__main__":
    main()
