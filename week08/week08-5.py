a = [9,8,7,6,5,4,3,2,1,0]
N = len(a)
print(a)  #排之前先印一下
for k in range(N):
  for i in range(1,N):
    if a[i] < a[i-1]: #比大小，不對的話
      a[i], a[i-1] = a[i-1], a[i]  #就左右交換
  print(a)  #排一輪之後，再印一下