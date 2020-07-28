#def my_function(x):
 #   return 5 * x

#print(my_function(7))
#def my_function(*kids):
 #   print("the youngest child is" + kids[2])

#my_function("emil","deva","momu")
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\n recursion example results")
tri_recursion(9)