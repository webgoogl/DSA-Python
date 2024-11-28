while True:
    n=int(input("Enter range : "))
    
    print("\n")

    print("<---- SELECT A PATTERN --->\n")
    print("1 -> SIMPLE\n2 -> HALF PYRAMID\n3 -> PYRAMID\n4 -> DIAMOND \n")

    select=int(input("Select : "))

    if select==1:
        
        for i in range(n):
            for k in range(n):
                print("*  ",end=" ")
            print("\n")
            
    elif select==2:
        
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="  ")
            for k in range(1*i+1):
                print("* ",end=" ")
            print("\n")
            
    elif select==3:
       
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="  ")
            for k in range(2*i+1):
                print("* ",end=" ")
            print("\n")


    elif select==4:
        
        for i in range(n):
            for j in range(n-i-1):
                print(" ",end="  ")
            for k in range(2*i+1):
                print("* ",end=" ")
            print("\n")

        a=n-1
        for i in range(a):
            for j in range(i+1):
                print(" ",end="  ")
            for k in range(2*a-i*2-1):
                print("* ",end=" ")
            print("\n")

    else:
        print("\nSomethings else wrong")

feed=input("Feedback :")
