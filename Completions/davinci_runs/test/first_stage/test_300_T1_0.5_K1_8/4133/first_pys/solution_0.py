

#import sys
#test_cases = open(sys.argv[1], 'r')
test_cases = open('test.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    test = test.replace('\n','')
    test = test.replace('?','')
    test = test.replace('(','')
    test = test.replace(')','')
    test = test.replace(':','')
    test = test.replace('-',' - ')
    test = test.replace('+',' + ')
    test = test.replace('*',' * ')
    test = test.replace('/',' / ')
    test = test.replace('>',' > ')
    test = test.replace('<',' < ')
    test = test.replace('.',' . ')
    test = test.split(' ')
    test = filter(None, test)
    #print test
    #print len(test)
    #print '\n'
    print test
    test_2 = []
    for i in range(len(test)):
        if test[i].isdigit():
            test_2.append(test[i])
        else:
            test_2.append(0)

    #print test_2
    #print len(test_2)
    #print '\n'

    for i in range(len(test)):
        if test[i] == '-':
            test_2[i-1] = int(test_2[i-1]) - int(test_2[i+1])
            test_2[i+1] = 0
        elif test[i] == '+':
            test_2[i-1] = int(test_2[i-1]) + int(test_2[i+1])
            test_2[i+1] = 0
        elif test[i] == '*':
            test_2[i-1] = int(test_2[i-1]) * int(test_2[i+1])
            test_2[i+1] = 0
        elif test[i] == '/':
            test_2[i-1] = int(test_2[i-1]) / int(test_2[i+1])
            test_2[i+1] = 0
        elif test[i] == '>':
            if int(test_2[i-1]) <= int(test_2[i+1]):
                print 'false'
                break
        elif test[i] == '<':
            if int(test_2[i-1]) >= int(test_2[i+1]):
                print 'false'
                break
        elif test[i] == '.':
            print ''.join(str(e) for e in test_2)
            #print test_2
            break

test_cases.close()