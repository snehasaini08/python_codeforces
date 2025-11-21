#A.Winter Sale
X,P = map(float, input().split())
#original price formula
original = P / (1 - X/100)

#Print with 2 decimal places
print(f"{original:.2f}")