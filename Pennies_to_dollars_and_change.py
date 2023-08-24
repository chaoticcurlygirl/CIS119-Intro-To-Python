print("ASSIGNMENT 01B - PENNIES TO DOLLARS AND CHANGE")
print("Developed by Chaoticcurlygirl at EC3PA for CIS119\n")
print(" This program will calculate the maximum number of dollars,\n and remaining quarters,dimes, nickles,\n and pennies that would be exchanged for a specified number of pennies.\n")
#Input
pennies = int(input("Enter the number of pennies: "))
#Process
startingPennies = pennies
dollars = pennies // 100 #exchange
pennies = pennies % 100 #left over
quarters = pennies //25 #exchange
pennies = pennies % 25 #left over
dimes = pennies // 10 #exchange
pennies = pennies % 10 #left over
nickles = pennies // 5 #exchange
pennies = pennies % 5 #left over
#Output
print("\nThe following would be given in exhange for those " + str(startingPennies) + " pennies:")
print(" Dollars:    " + str(dollars) )
print(" Quarters:   " + str(quarters) )
print(" Dimes:      " + str(dimes) )
print(" Nickles:    " + str(nickles) )
print(" Pennies:    " + str(pennies) )
print(" ") #print blank line
