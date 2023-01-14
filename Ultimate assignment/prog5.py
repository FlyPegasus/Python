#Occurance of India
str1="India"
teststr=str(input("Enter string: "))
#"INDIA India india INdIA iNdia"
lst=teststr.split(" ")
count=0
for i in range(len(lst)):
    if str1.upper()==lst[i].upper():
        count+=1
print("India appeared ",count," times.")
