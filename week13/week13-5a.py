a = list(map(int,input().split()))
N = len(a)-1
for i in range(N-1, -1, -1):
	print( a[i], end=' ')
print()