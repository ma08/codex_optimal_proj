
import sys;s=sys.stdin.readline;r=range;n,m=map(int,s().split());d=dict.fromkeys(r(1,m+1),0);exec('for i in r(n):\n for j in map(int,s().split()[1:]):\n  d[j]+=1\nprint(sum([1 for e in d.values() if e==n]))');
