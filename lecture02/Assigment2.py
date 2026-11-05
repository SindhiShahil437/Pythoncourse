cabin = input("Enter cabin class: ")

if cabin == "LUX":
    print("Upper-deck cabin.")
elif cabin == "A":
    print("Cabin above the car.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")