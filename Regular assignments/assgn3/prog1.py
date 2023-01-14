s=str(input("Enter string: "))
i=1
while i<len(s):
    if s[i-1]==s[i]:
        if len(s)==2:
            print("Empty String")
        s=s[:i-1]+s[i+1:]
    else:
        i+=1
print(s)
