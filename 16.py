num = float(raw_input("Enter the number of your choice > "))

diff = 0
if num > 17:
    diff = 2*(num - 17)

elif num <= 17:
    diff = 17 - num

print "The difference from 17 based upon the conditions is > ", diff 
