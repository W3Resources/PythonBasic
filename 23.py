str = raw_input("Enter the string > ")
num = int(input("Enter the number > "))

if len(str) < 2:
    print (str * num)
else:
    str1 = str[0:2]
    print str1 * num
