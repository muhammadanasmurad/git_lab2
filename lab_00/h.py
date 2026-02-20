x = input("Enter the flip: ")
h_solution = [1,2,3,4]
v_solution = [4,3,1,2]
final = []

for i in x.upper():
    if i == "H":
        final = h_solution
    else:
        final = v_solution
        

print(f"{final[0]} {final[1]}")
print(f"{final[3]} {final[2]}")
