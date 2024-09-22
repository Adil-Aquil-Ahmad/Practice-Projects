def password_Creation():
    a = input("enter a password: ")
    b = False
    c = False
    d = False
    e = False
    f = False
    for i in a:
     if i.isalpha():
        b = True
        if i.isupper():
           d = True
        elif i.islower():
           e = True
     elif i.isdigit():
        c = True

     elif i.isalnum()==False:
        f = True

        
    if b is False:
        print("please use alphabetic letters in the password")
    if c is False:
        print("please use numeric letters in the password")
    if d is False:
        print("please use uppercase letters in the password")
    if e is False:
        print("please use lowercase letters in the password")
    if f is False:
        print("please use symbols in the password")
    if b and c and d and e and f==True:
        print("your password is accepted")
        password_Creation()
    else:
        password_Creation()

password_Creation()        



        
    
    
