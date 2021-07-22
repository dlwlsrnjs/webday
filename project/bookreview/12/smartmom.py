# question=[]
# result=[]
# result_num=[]
# result_result=[]
# n=input()
# n=int(n)
# #첫번쨰 인풋
# question=input().split()
# #두번쨰인풋
# m=input()
# m=int(m)
# #세번쨰인풋
# result=input().split()
#
#
# for i in range(m):
#     for j in range(n):
#         if(question[j]==result[i]):
#             result_num=1
#             break
#         else:
#             result_num=0
#     if(result_num==1):
#         result_result.append('1')
#     else:
#         result_result.append('0')
#
#
# print(' '.join(result_result))
import sys

# len = int(input())
len=int(sys.stdin.readline())
# num1 = list(map(int,input().split()))
# num1=list(sys.stdin.readline(list(map(int,input().split()))))
num1=sys.stdin.readline().split()
# len = int(input())
# num2 = list(map(int,input().split()))
len=int(sys.stdin.readline())
num2=sys.stdin.readline().split()
ans = list(map(lambda n : n in num1, num2))
for _ in range(0, len):
    print("%d"%ans[_], end=" ")