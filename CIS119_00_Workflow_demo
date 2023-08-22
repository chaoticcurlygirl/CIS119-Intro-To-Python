# WORKFLOW DEMO (Prime Factors)
# Developed as a demo for cis 119
print("assignment 0 - Workflow Demo")
print("devloped by chaoticcurlygirl for Cis 119 at EC3PA (Fall A 2023)")
print("\n This Python program will determine and print the prime factors\n of an integer provided by the user. If the number provided is divisible\n only by 1 and itself, it will be marked as a Prime Number.\n")

num = 100
while num > 0:
    num = int(input("Enter a positive integer [or 0 to end]: "))
    if num !=0: #only do something if num is not 0
        primeFactors = str(num) + " =1" # start of output string
        prime = True # Boolean to track whether num is a prime number
        newNum = num #we will work with a copy of num called newNum
        #now loop through possible divisors from 2 to newNum
        for i in range(2,newNum) :
            # loop as long as newNum is evenly divisable by i
            while newNum % i == 0: # % return the remainder of int division
                prime = False #this is now NOT a prime number
                newNum = newNum / i # recalculate the newNum
                primeFactors += " x " + str(i) # add i to the list of factors
            # by nature only prime number will be evaluated as factors
        if prime: #if prime is still true
            primeFactors += " x " + str(num) # only divisible by 1 and itself
            print(str(num) + " is a PRIME NUMBER! " , end='')
        print(primeFactors)
    else:
        print("\nGood bye!") # end the program (user entered 0)
