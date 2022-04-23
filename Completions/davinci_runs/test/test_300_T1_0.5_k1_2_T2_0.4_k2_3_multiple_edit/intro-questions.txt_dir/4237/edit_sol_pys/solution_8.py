

def main():
	a,b,c,d=map(int,input().split())
	ans=b-a+1
	ans-=(b//c-(a-1)//c) #cの倍数
	ans-=(b//d-(a-1)//d) #dの倍数
	ans+=(b//(c*d)-(a-1)//(c*d)) #c*dの倍数
	print(ans)

if __name__=="__main__":
	main()
