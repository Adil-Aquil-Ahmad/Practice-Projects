def Roman_No():
    while True: 
        try:
            x=0
            Roman = str(input("Enter a Roman No."))
            if Roman.isalpha()==False:
                print("Thats not a Valid Roman No.")
                continue
                
            List_Roman = ["I","V","X","L","C","M","D"]
            for i in List_Roman:
                if i in Roman:
                 x+=1
                 break
            else:
                x-=1
                
            if x<1:
                print("Thats not a Valid Roman No.")
                Roman_No()
                
                
        except ValueError: 
            print("Invalid input. Please enter an integer.")
        Sum = 0
        Roman_Dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        j=0
        for j in range(0,(len(Roman))):
            if Roman[j]=="I":
                Sum+=1
                j+=1
            elif Roman[j]=="V":
                Sum+=5
                j+=1
            elif Roman[j]=="X":
                Sum+=10
                j+=1
            elif Roman[j]=="L":
                Sum+=50
                j+=1
            elif Roman[j]=="C":
                Sum+=100
                j+=1
            elif Roman[j]=="D":
                Sum+=500
                j+=1
            elif Roman[j]=="M":
                Sum+=1000
                j+=1
        for x in range(1, (len(Roman))):
            if Roman[x]=="M" and (Roman[x-1]=="L" or Roman[x-1]=="X" or Roman[x-1]=="V" or Roman[x-1]=="D" or Roman[x-1]=="I"):
                print("Thats not a Valid Roman no.")
                Roman_No()
            elif Roman[x]=="M" and Roman[x-1]=="C":
                if x in range(2, (len(Roman))):
                    if Roman[x]=="M" and (Roman[x-2]=="L" or Roman[x-2]=="X" or Roman[x-2]=="V" or Roman[x-2]=="D" or Roman[x-2]=="I" or Roman[x-2]=="C"):
                        print("Thats not a Valid Roman no.")
                        Roman_No()
                    else:
                        Sum-=200
                else:
                    Sum-=200
            if Roman[x]=="C" and (Roman[x-1]=="L" or Roman[x-1]=="V" or Roman[x-1]=="I"):
                print("Thats not a Valid Roman no.")
                Roman_No()
            elif Roman[x]=="C" and Roman[x-1]=="X":
                if x in range(2, (len(Roman))):
                    if Roman[x]=="C" and (Roman[x-2]=="L" or Roman[x-2]=="X" or Roman[x-2]=="V" or Roman[x-2]=="I"):
                        print("Thats not a Valid Roman no.")
                        Roman_No()
                    else:
                        Sum-=20
                else:
                    Sum-=20
            if Roman[x]=="L" and (Roman[x-1]=="L" or Roman[x-1]=="V" or Roman[x-1]=="I"):
                print("Thats not a Valid Roman no.")
                Roman_No()
            elif Roman[x]=="L" and Roman[x-1]=="X":
                if x in range(2, (len(Roman))):
                    if Roman[x]=="L" and (Roman[x-2]=="L" or Roman[x-2]=="X" or Roman[x-2]=="V" or Roman[x-2]=="I"):
                        print("Thats not a Valid Roman no.")
                        Roman_No()
                    else:
                        Sum-=20
                else:
                    Sum-=20
            if Roman[x]=="D" and (Roman[x-1]=="L" or Roman[x-1]=="X" or Roman[x-1]=="V" or Roman[x-1]=="D" or Roman[x-1]=="I"):
                print("Thats not a Valid Roman no.")
                Roman_No()
            elif Roman[x]=="D" and Roman[x-1]=="C":
                if x in range(2, (len(Roman))):
                    if Roman[x]=="D" and (Roman[x-2]=="L" or Roman[x-2]=="X" or Roman[x-2]=="V" or Roman[x-2]=="I" or Roman[x-2]=="C"):
                        print("Thats not a Valid Roman no.")
                        Roman_No()
                    else:
                        Sum-=200
                else:
                    Sum-=200
            if Roman[x]=="X" and (Roman[x-1]=="V"):
                print("Thats not a Valid Roman no.")
                Roman_No()
            elif Roman[x]=="X" and Roman[x-1]=="I":
                if x in range(2, (len(Roman))):
                    if Roman[x]=="X" and (Roman[x-2]=="V" or Roman[x-2]=="I"):
                        print("Thats not a Valid Roman no.")
                        Roman_No()
                    else:
                        Sum-=2
                else:
                    Sum-=2
            if Roman[x]=="V" and (Roman[x-1]=="V"):
                print("Thats not a Valid Roman no.")
                Roman_No()
            elif Roman[x]=="V" and Roman[x-1]=="I":
                if x in range(2, (len(Roman))):
                    if Roman[x]=="V" and (Roman[x-2]=="V" or Roman[x-2]=="I"):
                        print("Thats not a Valid Roman no.")
                        Roman_No()
                    else:
                        Sum-=2
                else:
                    Sum-=2
        print(Sum)
               
Roman_No()
    
        
    
    
        
     
    
        
