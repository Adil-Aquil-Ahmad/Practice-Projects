a =  input("enter no. seperated by space")
b = a.split()
for i in range(len(b)):
    b[i]= int(b[i])
b.remove(max(b))
print(max(b))




            
        
