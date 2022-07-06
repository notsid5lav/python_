x=[1,2,3,4,5,6,7,8,9,10] #declare a filled array 
a=[]                     #declare two empty arrays 
b=[]

for i in x:              #declare a for loop for checking values in x
    if(i%2==0):          #if the number is even then it is transferd to a or b othwerwise 
	a.append(i)
    else:
        b.append(i)

print(a)                 #print both the output of arrays a and b
print(b)
