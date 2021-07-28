import sys

numbers=[]
number = input()
number = int(number)
if (1 <= number <= 100):
    for i in range(number):
        numbers.append(input().split())
    print(numbers)
    numbers.sort()
    print(numbers)
else:
    print("error")
for q in range(number):
    print(numbers[q][0],numbers[q][1])
