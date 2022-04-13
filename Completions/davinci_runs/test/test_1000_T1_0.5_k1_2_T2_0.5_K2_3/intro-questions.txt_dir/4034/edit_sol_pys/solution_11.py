//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = (char *)malloc(sizeof(char) * 100001);
    char *t = (char *)malloc(sizeof(char) * 100001);
    scanf("%s", s);
    scanf("%s", t);
    int len = strlen(s);
    int i, j;
    int flag = 0;
    for (i = 0; i < len; i++)
    {
        if (s[i] == t[i])
        {
            continue;
        }
        else
        {
            for (j = i + 1; j < len; j++)
            {
                if (s[j] == t[i])
                {
                    flag += j - i;
                    break;
                }
            }
            if (j == len)
            {
                printf("-1");
                return 0;
            }
            for (; j > i; j--)
            {
                char tmp = s[j];
                s[j] = s[j - 1];
                s[j - 1] = tmp;
                flag++;
            }
        }
    }
    printf("%d", flag);

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())

def solve(s):
    last = 'a'
    for i in range(len(s)):
        if s[i] < last:
            s[i] = '1'
        else:
            s[i] = '0'
            last = s[i]
    return ''.join(s)

if s == sorted(s):
    print 'YES'
    print '0' * n
else:
    print 'YES'
    print solve(s)
