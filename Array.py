arr=[]
n=int(input("enter the range of array"))
for i in range (0,n):
    x= int(input("Enter array element"))
    arr.append(x)

print("entered array element",arr)
print("Maximum number is",max(arr))
print("sum of array elements",sum(arr))
print("sorted array ",sorted(arr))
print("average entered element in list",sum(arr)/5)

