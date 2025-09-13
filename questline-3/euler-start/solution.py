total=0
num=1000
for i in range(num):
   if (i%3==0) or (i%5==0):
        total=total+i
   else:
        continue
#print("Sum of all multiples of 3 or 5 below 1000=" , total)


n=600851475143
factors=[]
for i in range(2,n+1):
    if n%i==0:        
        factors.append(i) 
        n=n//i        
    if n==1:            
        break
print("Prime factors:",factors)
print("Largest factor:",factors[-1])

