red,green,blue=input().split()
red=int(red)
green=int(green)
blue=int(blue)
total=[0][0][0]
print(red,green,blue)

for i in red:
    total[0][0][i]=i
    count=+1

print(total)