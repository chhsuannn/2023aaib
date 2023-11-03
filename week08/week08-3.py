a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
N = len(a)  
for i in range(1,N):  #這個迴圈從1開始   
  print('現在檢查', a[i],a[i-1])
  if a[i]-a[i-1] !=a[1]-a[0]:  #某兩項相減，和最前面的2項相減
    print('失敗',a[i],a[i-1])  #那就是失敗
    #return False
print('程式檢查結束囉!')