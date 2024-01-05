a= list(map(int,input().split()))
ans=0
for b in a:
	if b>0:	ans += b
print(ans,end='')