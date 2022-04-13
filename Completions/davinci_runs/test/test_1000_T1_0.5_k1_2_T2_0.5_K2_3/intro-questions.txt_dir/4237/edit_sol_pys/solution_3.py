
def main():
	a,b,c,d=map(int,input().split())
	ans=b-a+1
	ans-=(b//c-(a-1)//c)
	ans-=(b//d-(a-1)//d)
	ans+=(b//(c*d)-(a-1)//(c*d)) #被c,d共通で割り切れる数を引いて加算
	print(ans)

if __name__=="__main__":
	main()
