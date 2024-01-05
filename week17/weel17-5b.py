x1,y1,x2,y2 = list(map(int,input().split()))
ans = (x1-x2) * (y1-y2)
if ans <0: 
	ans = -ans
print(ans,end='')