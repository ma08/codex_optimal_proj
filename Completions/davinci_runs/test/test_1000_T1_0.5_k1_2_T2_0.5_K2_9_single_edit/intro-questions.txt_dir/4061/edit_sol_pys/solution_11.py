
def solve(string):
    stack = [string[0]]
    for c in string[1:]:
        if c >= stack[-1]:
            stack.append(c)
        else:
            for i in xrange(len(stack)):
                if c < stack[i]:
                    stack[i] = c
                    break
    return ''.join(stack)
    
for i in xrange(input()):
    print 'Case #%d: %s' % (i+1, solve(raw_input()))
