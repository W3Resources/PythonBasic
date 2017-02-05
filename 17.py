num = float(raw_input("Enter the number > "))

if abs(1000-num) < 100:
    print "Its within 100 of 1000"
elif abs(2000-num) < 100:
    print "Its withing 100 of 2000"
else:
    print "Its not within 100 of 1000 or 2000"
