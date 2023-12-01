n = int(input())
print(n,end=' ')

if n%400==0:  print('is a leap year.')
elif n%100==0:  print('is not a leap year.')
elif n%4==0:  print('is a leap year.')
else:  print('is not a leap year.')