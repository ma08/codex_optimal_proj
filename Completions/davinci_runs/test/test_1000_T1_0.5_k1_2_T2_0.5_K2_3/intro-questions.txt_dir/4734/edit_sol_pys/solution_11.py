
def main():y,p=input().split();print(y+'x'+p if y[-1]=='e'else y[:-1]+'ex'+p if y[-1]in'aiou'else y+p if y[-2:]=='ex'else y+'ex'+p)
main() 
