

def main():
	a,b,c,d=map(int,input().split()) #a,b,c,dを入力
	ans=b-a+1
	ans-=(b//c-(a-1)//c) #aからbまでのcの倍数を引く
	ans-=(b//d-(a-1)//d) #aからbまでのdの倍数を引く
	ans+=(b//(c*d)-(a-1)//(c*d)) #aからbまでのcとdの公倍数を足す
	print(ans)

if __name__=="__main__":
	main()
