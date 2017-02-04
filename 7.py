fname = raw_input("Enter the file name > ")

if "." in fname:
    list = fname.split(".")
    print list[1]

else:
    print "This file does not have any extension"
