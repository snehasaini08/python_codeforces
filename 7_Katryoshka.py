n, m, k = map(int,input().split()) #98,24,89
use_mouth = min(m,k,n) #24
n -= use_mouth
m -= use_mouth
k -= use_mouth  #66,0,65
use_no_mouth = min(n // 2,k)
print(use_mouth + use_no_mouth) 
use_no_mouth = min(n // 2,k)
print(use_mouth + use_no_mouth)
