#palindromes in a list
import math
def Palin(num):
    temp=num
    i=len(str(num))
    rev=0
    while temp!=0:
        rev=rev+math.pow(10,i-1)*(temp%10)
        temp=temp-(temp%10)
        temp=temp/10
        i=i-1
    if rev==num:
        return 1
    else:
        return 0
lst=[]
final=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    lst+=[int(input("Enter number: "))]
print("Entered list: ",lst)
for j in range(n):
    if Palin(lst[j]):
        final+=[lst[j]]
print("Palindromes present are: ",final)
