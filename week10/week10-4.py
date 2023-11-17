a = int(input())

if a <= 2000: 
	ans=100
else: #more than 2000
	ans=100
	more = a-2000  #多多少公尺
	ans += more//500*5  #每500再跳一次5元
	if more%500:  #有500的餘數的話，再跳一次5元
		ans+=5

print(ans)