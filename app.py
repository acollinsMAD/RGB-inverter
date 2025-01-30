#defines variables R, G and B to user input
R = int(input("Enter the value of Red: "))
G = int(input("Enter the value of Green: "))
B = int(input("Enter the value of Blue: "))

#takes inputted values and returns the inverted values
def inversionFormula(R, G, B):
    # Inversion formula
    R1 = 255 - R
    G1 = 255 - G
    B1 = 255 - B
    return R1, G1, B1

#prints inverted values to console
print (inversionFormula(R, G, B))