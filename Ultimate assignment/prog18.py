test="The quick Brown Fox"
ucount=0
lcount=0
for i in range(len(test)):
    if test[i].isupper():
        ucount+=1
    elif test[i].islower():
        lcount+=1
print(ucount,lcount)
