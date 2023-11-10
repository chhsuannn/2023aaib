a = input().split()
N = int(a[0])
ans = 0

for i in range(1, N+1):
	ans += int(a[i])
	
print(ans)