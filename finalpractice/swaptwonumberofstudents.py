# we assume code is wronng iitially
code1 = input("Enter Student A's locker code: ")
code2 = input("Enter Student B's locker code: ")

print("\nBefore Swap:")
print("Student A's locker code:", code1)
print("Student B's locker code:", code2)


temp = code1
code1 = code2
code2 = temp

print("\nAfter Swap:")
print("Student A's locker code:", code1)
print("Student B's locker code:", code2)
