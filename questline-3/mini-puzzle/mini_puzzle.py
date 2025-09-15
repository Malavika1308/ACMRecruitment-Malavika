def rotate_binary(n,k):
    x=n[k:]+n[:k]
    return int(x,2)
n=input("Enter your binary number:")
k=int(input("Enter how many steps do you want to rotate:"))
result=rotate_binary(n,k)
print("Your new string:" , result)


#outputs

#Enter your binary number:1011
#Enter how many steps do you want to rotate:2
#Your new string: 14


