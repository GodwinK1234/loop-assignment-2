num = int (input("Enter the value of n: "))

contain = num

sum = 0

if num <=0:
    print("Enter a whole positive number")
else:
            while num>0:
                sum = sum + num
                num = num -1;
                print("Sum of first", contain, "natural numbers is: ", sum)
