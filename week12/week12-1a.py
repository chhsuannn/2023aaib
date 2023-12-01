#分式化簡 瘋狂城設裡
a = 51
b = 68

def gcd(a,b):
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)
ans = gcd(a,b)
print(a//ans, b//ans)