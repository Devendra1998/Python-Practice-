print("enter a number")
x=int(input())
if x>1:
 for i in range(2,x):
     if(x % i) == 0:
         print(x,"number is not prime")
 else:
     print(x,"number is prime")
