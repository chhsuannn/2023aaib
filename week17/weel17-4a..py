a= int(input())
ten=1
while a>0:
	print(a%10*ten,end=' ')
	ten = ten*10
	a = a//10