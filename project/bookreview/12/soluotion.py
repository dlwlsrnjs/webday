n=input()
n=int(n)
print(n)

result = []
for i in range(2,n+1):
    while(n%i==0):
        n/=i
        result.append(i)
        i+=1


for j in range(result):
    print(result[j],result[j+1])