N = int(input())  #17

a = [0,1]
for i in range(2,N+1):
	a.append(a[i-1]+a[i-2])

for i in range(N,-1,-1):
	#print(a[i])
	print(f'f({i})={a[i]}')