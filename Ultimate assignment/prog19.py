#prime factors of an Integer
num=int(input("Enter your number: "))
lst=[]
for i in range(2,num):
    if num%i==0:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag+=1
                break
        if flag==0:
            lst+=[i]
print("Prime factors of ",num," are: ",end="")
#for k in range(len(lst)):
#    print(lst[k],",",end="")
print(lst)
