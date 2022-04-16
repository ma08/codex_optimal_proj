

import sys

sys.setrecursionlimit(1000000)


def dfs(u):
	if used[u]:
		return
	used[u] = True
	for v in g[u]:
		dfs(v)


def dfs2(u):
	if used2[u]:
		return
	used2[u] = True
	for v in g2[u]:
		dfs2(v)


def dfs3(u):
	if used3[u]:
		return
	used3[u] = True
	for v in g3[u]:
		dfs3(v)


def dfs4(u):
	if used4[u]:
		return
	used4[u] = True
	for v in g4[u]:
		dfs4(v)


def dfs5(u):
	if used5[u]:
		return
	used5[u] = True
	for v in g5[u]:
		dfs5(v)


def dfs6(u):
	if used6[u]:
		return
	used6[u] = True
	for v in g6[u]:
		dfs6(v)


def dfs7(u):
	if used7[u]:
		return
	used7[u] = True
	for v in g7[u]:
		dfs7(v)


def dfs8(u):
	if used8[u]:
		return
	used8[u] = True
	for v in g8[u]:
		dfs8(v)


def dfs9(u):
	if used9[u]:
		return
	used9[u] = True
	for v in g9[u]:
		dfs9(v)


def dfs10(u):
	if used10[u]:
		return
	used10[u] = True
	for v in g10[u]:
		dfs10(v)


def dfs11(u):
	if used11[u]:
		return
	used11[u] = True
	for v in g11[u]:
		dfs11(v)


def dfs12(u):
	if used12[u]:
		return
	used12[u] = True
	for v in g12[u]:
		dfs12(v)


def dfs13(u):
	if used13[u]:
		return
	used13[u] = True
	for v in g13[u]:
		dfs13(v)


def dfs14(u):
	if used14[u]:
		return
	used14[u] = True
	for v in g14[u]:
		dfs14(v)


def dfs15(u):
	if used15[u]:
		return
	used15[u] = True
	for v in g15[u]:
		dfs15(v)


def dfs16(u):
	if used16[u]:
		return
	used16[u] = True
	for v in g16[u]:
		dfs16(v)


def dfs17(u):
	if used17[u]:
		return
	used17[u] = True
	for v in g17[u]:
		dfs17(v)


def dfs18(u):
	if used18[u]:
		return
	used18[u] = True
	for v in g18[u]:
		dfs18(v)


def dfs19(u):
	if used19[u]:
		return
	used19[u] = True
	for v in g19[u]:
		dfs19(v)


def dfs20(u):
	if used20[u]:
		return
	used20[u] = True
	for v in g20[u]:
		dfs20(v)


def dfs21(u):
	if used21[u]:
		return
	used21[u] = True
	for v in g21[u]:
		dfs21(v)


def dfs22(u):
	if used22[u]:
		return
	used22[u] = True
	for v in g22[u]:
		dfs22(v)


def dfs23(u):
	if used23[u]:
		return
	used23[u] = True
	for v in g23[u]:
		dfs23(v)


def dfs24(u):
	if used24[u]:
		return
	used24[u] = True
	for v in g24[u]:
		dfs24(v)


def dfs25(u):
	if used25[u]:
		return
	used25[u] = True
	for v in g25[u]:
		dfs25(v)


def dfs26(u):
	if used26[u]:
		return
	used26[u] = True
	for v in g26[u]:
		dfs26(v)


def dfs27(u):
	if used27[u]:
		return
	used27[u] = True
	for v in g27[u]:
		dfs27(v)


def dfs28(u):
	if used28[u]:
		return
	used28[u] = True
	for v in g28[u]:
		dfs28(v)


def dfs29(u):
	if used29[u]:
		return
	used29[u] = True
	for v in g29[u]:
		dfs29(v)


def dfs30(u):
	if used30[u]:
		return
	used30[u] = True
	for v in g30[u]:
		dfs30(v)


def dfs31(u):
	if used31[u]:
		return
	used31[u] = True
	for v in g31[u]:
		dfs31(v)


def dfs32(u):
	if used32[u]:
		return
	used32[u] = True
	for v in g32[u]:
		dfs32(v)


def dfs33(u):
	if used33[u]:
		return
	used33[u] = True
	for v in g33[u]:
		dfs33(v)


def dfs34(u):
	if used34[u]:
		return
	used34[u] = True
	for v in g34[u]:
		dfs34(v)


def dfs35(u):
	if used35[u]:
		return
	used35[u] = True
	for v in g35[u]:
		dfs

n = int(input())

a = list(map(int, input().split()))

if n < 2:
	print("YES\n0")
	exit()

if a[0] > a[1]:
	print("NO")
	exit()

for i in range(1, n-1):
	if a[i] < a[i-1] and a[i] > a[i+1]:
		print("NO")
		exit()

if a[-1] < a[-2]:
	print("NO")
	exit()

print("YES")

for i in range(n):
	if a[i] > a[i-1]:
		print("0 ", end="")
	else:
		print("1 ", end="")
