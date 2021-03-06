

def getAlloc(sal, inv, eq, cry, deb):   # Method to allocate funds
    reccInv = 0.25 * sal    # Recommended Investment based on the Salary
    print("Recommended investment for your salary is INR ", reccInv)
    if inv < reccInv:
        print("The investment deficit is INR ", reccInv - inv)
    allocEq = inv * 0.01 * eq
    allocCry = inv * 0.01 * cry
    allocDeb = inv * 0.01 * deb
    print("You should allocate INR ", allocEq, "in Equity  \nINR ", allocCry, " in Crypto \nINR ", allocDeb, " in Debt")


2

def sipCalculator(target, ror, years, inf):
    if inf == "Y":
        ror = ror - 6   # Inflation adjusted Rate of return
    mror = ror/1200     # Calculates Monthly rate of return
    nMonths = years * 12    # Calculates no. of months
    reqSIP = (target * mror)/((1 + mror) * ((pow((1 + mror), nMonths)) - 1))  # Calculates SIP amount required
    print("The required monthly SIP to accumulate amount INR ", target," in ", years," years is \nMonthly SIP in INR = ", reqSIP)



def lumpsumCalculator(target, ror, years, inf):
    if inf == "Y":
        ror = ror - 6
    ror = ror/100
    reqLumpsum = target / pow((1 + ror), years)  # Calculates Lumpsum amount required
    print("The required Lumpsum amount to accumulate amount INR ", target," in ", years," years is \nLumpsum amount in INR = ", reqLumpsum)



# Main Code Starts
print("Welcome to Pendse Investment Services \nThis application provides 2 Services: \n1. Investment Allocation "
      "calculator \n2. Goal based SIP/Lumpsum Calculator")
continueLoop = True
while continueLoop:
    choiceService = int(input("Which service would you like to choose?\n1 : Investment Allocation\n2 : Goal "
                              "Planning\n3: Exit\n"))

    if choiceService == 1:
        print("You have selected the Investment planning module")
        ageUser = int(input("Please enter your age "))
        salUser = float(input("Please enter your monthly Salary in INR "))
        invUser = float(input("Please enter the amount to invest in INR "))
        print(
            "Recommended fund allocation is as follows \n Allocation percentage in Equity = 100 - Your age \n Allocation "
            "percentage in Crypto = 5 \n Allocation percentage in Debt = 100 - (Equity + Crypto)")
        print("Continue with recommended Allocation?")
        eqPerc = 100 - ageUser
        cryPerc = 5
        debPerc = 100 - (eqPerc + cryPerc)
        choice = input("Press Y or N")
        if choice == 'Y':
            getAlloc(salUser, invUser, eqPerc, cryPerc, debPerc)

        else:
            print("Please enter your allocation percentage for Equity, Crypto and Debt")
            eqPercUser = int(input("Equity allocation -"))
            cryPercUser = int(input("Crypto allocation - "))
            debtPercUser = 100 - (eqPercUser + cryPercUser)
            getAlloc(salUser, invUser, eqPercUser, cryPercUser, debtPercUser)



    elif choiceService == 2:
        print("Welcome to the Goal Planning module")
        targAmount = float(input("Please enter your target amount "))
        timePeriod = int(input("Please enter the number of years till maturity "))
        rateReturn = float(input("Please enter the expected rate of return in percentage "))  # Nominal Rate of Return
        print("Do you want to adjust your SIP/Lump sum amount for inflation?(Inflation rates assumed to be 6%) ")
        choiceInf = input("Please enter Y for yes N for No ")
        print("Enter your Mode of investment, 1 for monthly SIP or 2 for Lumpsum amount")
        choiceMode = int(input())
        if choiceMode == 1:
            sipCalculator(targAmount, rateReturn, timePeriod, choiceInf)
        elif choiceMode == 2:
            lumpsumCalculator(targAmount, rateReturn, timePeriod, choiceInf)



    elif choiceService == 3:
        print("Thank You for using our Services")
        continueLoop = False