print("ASSIGNMENT 01A - TRIANGLE CALCULATOR")
print("Developed by Chaoticcurlygirl at EC3PA for CIS119")
print("\n This program will calculate the hypotenuse legnth of a right triangle,\n and the perimeter (sum of all three sides) \n given the legnth of the side A & B provided by the user \n")

#Triangle formula for hypotenuse is C equals the square root of A squared plus B squared
#Input , note to self:  this is what we get from the user
sideA = float(input("Enter the legnth of side A: "))
sideB = float(input("Enter the legnth of side B: "))
#Process , note to self: This is how we get our output
sideC = ((sideA**2) + (sideB**2)) ** 0.5
area = sideA * sideB * 0.5
perimeter = sideA + sideB + sideC;
#Output , note to self: the solution to the equation
print("The legnth of the hypotrnuse is ", end = ' ') 
print(format(sideC, '0.2f'))
print("the area is " + format(area, '0.02f'))
print("The perimeter is " + format(perimeter, '0.2f'))
