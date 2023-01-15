# Alphabet pattern
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input("Enter a number upto 26: "))
for i in range(n+1):
    for j in range(i):
        print(alpha[j],end=" ")
    print()
