color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
c = set()
for item in color_list_1:
    if item not in color_list_2:
        c.add(item)
print c
