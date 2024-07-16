text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

print("The code prints different values on lines 3 and 4 because in line 3, its searching from index 21 which is the start point, while the start point for line 4 is at 0.")