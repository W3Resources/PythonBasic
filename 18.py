num1 = int(raw_input("Enter the first value > "))
num2 = int(raw_input("Enter the second value > "))
num3 = int(raw_input("Enter the third value > "))
sum = num1 + num2 + num3

if (num1 == num2 and num2 == num3 and num3 == num1):
    print "Thrice of their sum is > ", 3*sum
else:
    print "Their sum is > ", sum
