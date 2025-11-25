# J.Multiples
A,B=map(int,input().split())

#check kro multiples hai ya nahi
if A % B == 0 or B % A == 0:
    print("Multiples")
else:
    print("No Multiples")    