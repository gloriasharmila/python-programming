a=int(input())
b=int(input())
for i in range(a,b):
sum=0
temp=i
if temp>0:
digit=temp%1
sum+=digit ** 3
temp//=10
if i==sum:
print(i)
