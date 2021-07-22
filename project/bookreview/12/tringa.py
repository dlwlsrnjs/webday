a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if(a==b==c):
    print("정삼각형")
elif(a==b or b==c or a==c):
    if not(a<b+c and b<c+a and c<a+b):
        print("삼각형아님")
    else:
        print("이등변삼각형")
elif((a*a)+(b*b)==c*c):
    print("직각삼각형")
elif(a<b+c and b<c+a and c<a+b):
    print("삼각형")
else:
    print("삼각형아님")
