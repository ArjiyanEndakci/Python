###Even Odd Negative Positive
num=int(input("Enter Number:"))
if num>0:
    if num%2==0:
     print("Even and Positive")
    else:
        print("Odd and Positive")
if num <0:
    if num%2==1:
        print("Odd and Negative")    
    else:
        print("Even and Negative")