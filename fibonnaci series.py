x=int(input("enter no of terms"))
i = 0
j = 1
count = 0
print("fibbonaci series upto nterms",x)
while count < x:
    print(i,end=',')
    k = i + j
    i = j
    j = k
    count += 1