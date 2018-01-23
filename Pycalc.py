def pycal():
    x=input("Enter First No.")
    y=input("Enter Second No.")
    test=1
    print("Python Calculator\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponent")
    while(test==1):
        case=input("Enter your choice: ")                                                                                                        
        if(case==1):
            z=x+y
        elif(case==2):
            z=x-y
        elif(case==3):
            z=x*y
        elif(case==4):
            z=x/y
        elif(case==5):
            z=x%y
        elif(case==6):
            z=x**y
        else:
            case=0
            print("Invalid choice!!!")
        if(case!=0):    
            print(z)
        test=input("Want to play more with entered numbers(1/0)")
    
