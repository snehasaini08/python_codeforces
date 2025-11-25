# o. Calculator
# Input lo (jaise "7+54" ya "17*10")
expr = input()
# operator check kr k split kro
if '+' in expr:
    A, B = expr.split('+')
    print(int(A) + int(B))
elif '-' in expr:
    A, B = expr.split('-')
    print(int(A) - int(B))
elif '*' in expr:
    A, B = expr.split('*')
    print(int(A) * int(B))
elif '/' in expr:
    A, B = expr.split('/')
    print(int(A) // int(B)) # integer division