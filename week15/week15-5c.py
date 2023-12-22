a = input()
ans = [0]*7
for c in a:
	for i in range(1,7):
		if c==str(i): ans[i] += 1
for i in range(1,7):
	print(i,':',ans[i],sep='')