# Description: the one stop insurance company needs a program to calculate new policy information
# Author: Ben Legge
# Date(s): Nov. 15, Nov. 19, Nov. 20, Nov. 21, Nov. 22, Nov. 25


# Define required libraries.
import datetime
import re
import decimal
import sys
import time

# Define program constants.
PolNumber = 1944
BasicPrem = 869.00
AddCar = 0.25
LiabalCover = 130.00
GlassCover = 86.00
LoanCar = 58.00
HST_RATE = 0.15
ProcessFee = 39.99


# Define program functions.
def Guide():
    print(f"    1    2    3    4    5    6    7    8    9    0    ")

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):

    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

    
        

def PrevClaim():
    ClaimN = [1844, 1843, 1799]
    ClaimD = [datetime.datetime(2024, 11, 19).date(), datetime.datetime(2024, 11, 19).date(), datetime.datetime(2024, 11, 11).date()]
    ClaimA = [13000, 13550, 16000]
    print(f"     Claim #     Claim Date          Amount")
    print(f"     --------------------------------------")
    print(f"     {ClaimN[0]}        {ClaimD[0]}       {ClaimA[0]:,.2f}")
    print(f"     {ClaimN[1]}        {ClaimD[1]}       {ClaimA[1]:,.2f}")
    print(f"     {ClaimN[2]}        {ClaimD[2]}       {ClaimA[2]:,.2f}")
    
Provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'ON', 'PE', 'QC', 'SK', 'NU', 'YT']
FMDP = ['Full', 'Monthly', 'Down Pay']

# Main program starts here.
while True:
    TotalIterations = 30
    Message = "Loading..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
    
    print()
    print()
    CustName = input("Enter name, first and last:  ")
    CustName = CustName.title()
    Address = input("Enter street address:  ")
    City= input("Enter city:  ")
    City = City.title()
    while True:
        Province = input("Enter province(EX: NL):  ")

        Province = Province.upper()

        if Province in Provinces:
            break
        else:
            print("Please enter valid province.")
            continue
    
    Postal = input("Enter postal code:  ")
    Phone = input("Enter phone number:  ")
    print()
    Car = input("Number of cars being insured:  ")
    Car = int(Car)

    Liable = input("Opt in for extra liability?(Y/N):  ")
    Liable = Liable.upper()

    Glass = input("Opt in for glass coverage?(Y/N):  ")
    Glass = Glass.upper()

    Loaner = input("Opt in for loaner car?(Y/N):  ")
    Loaner = Loaner.upper()

    while True:
        Payment = input("Would you like to pay in Full or Monthly installments? Enter Down Pay to make a down payment:  ")

        Payment = Payment.title()

        if Payment in FMDP:
            break
        else:
            print("Please enter valid payment choice.")
            continue
    
    if Payment == "Down Pay":
        Down = input("Enter down payment amount:  ")
        Down = int(Down)

 #Calculations

    if Car > 1:
        Discount = BasicPrem * AddCar
    
    if Car > 1:
        DiscountedPrem = BasicPrem - Discount
    
    if Car > 1:
        RealPrem = BasicPrem + DiscountedPrem * Car
    
    if Car < 1:
        RealPrem = BasicPrem
    

    if Liable == "Y":
        Liability = LiabalCover * Car
    elif Liable == "N":
        Liability = 0.00
    elif Liability > 1000000:
        Liability = 1000000
    
    if Glass == "Y":
        CarGlass = GlassCover * Car
    else: 
        CarGlass = 0

    if Loaner == "Y":
        CarLoan = LoanCar * Car
    else:
        CarLoan = 0
    
    ExtraCost = Liability + CarGlass + CarLoan

    TotalPrem = RealPrem + ExtraCost

    Tax = TotalPrem * HST_RATE

    TotalCost = TotalPrem + Tax

    if Payment == "Down Pay":
        Monthly = (TotalCost + 39.99) / 8 - Down
    else:
        Monthly = (TotalCost + 39.99) / 8
    
    Invoice = datetime.datetime.now().date()
    FirstPay = Invoice + datetime.timedelta(days=30)

    
    #Results I think

    Guide()
    print(f"     {CustName}              #{PolNumber}")
    print(f"     {Address}  {City}   {Province}  {Postal}")
    print(f"                 {Phone}")
    print(f"     ---------------------------------------------")
    print()
    print(f"     Car's insured: {Car}   ")
    print(f"     Opted for liability: {Liable}")
    print(f"     Opted for glass coverage:  {Glass}")
    print(f"     Opted for loaner car:  {Loaner}")
    print()
    print(f"             Payment chosen: {Payment}")
    print()
    print(f"     ----------------------------------------------")
    print()
    print(f"     Premiums: ${RealPrem:,.2f}")
    if Liable == "Y":
        print(f"     Liability: ${Liability:,.2f}")

    if Glass == "Y":
        print(f"     Glass: ${CarGlass:,.2f}")
    
    if Loaner == "Y":
        print(f"     Loaner car: ${CarLoan:,.2f}")
    
    print(f"     Premium total: ${TotalPrem:,.2f}")
    print(f"     HST: ${Tax:,.2f}")
    print()
    print(f"     -----------------------------------------------")
    print()
    print(f"     Please note that all coverage plans only")
    print(f"     support liability up to $1,000,000 as ")
    print(f"     outlined in our policy. ")
    print()
    print()
    if Payment == "Full":
        print(f"     Total cost: ${TotalCost:,.2f}")
    else:
        print(f"     Monthly payment: ${Monthly:,.2f}")

    if Payment == "Down Pay":
        print(f"     Down payment made: ${Down:,.2f}")

    if Payment != "Full":
        print(f"     Invoice date: {Invoice} Date of first payment: {FirstPay}")
    
    print()
    print(f"     --------------------------------------------------")
    print()
    PrevClaim()
    print()
    print()

    Repeat = input("Would you like to enter another claim?(Y/N):  ")
    Repeat = Repeat.upper()

    if Repeat == "N":
        break
