#import math library 
import math
#Let user input the numerator 
while True:
 num = eval(input("Enter a numerator: Value must be greater than 0: "))
 if  num > 0:
     break
 else:
     print ("Value must be greater than 0. Please re-enter the numerator. ")
     continue
#Let user enter the denominator 
while True:
 denom = eval(input("Enter a denominator: Value must be greater than 0: "))
 if  denom > 0:
     break
 else:
     print ("Value must be greater than 0. Please re-enter the numerator. ")
     continue
#using gdc math module 
gcd = math.gcd(num,denom)
numgcd= num//gcd
degcd = denom//gcd
wholenum = num//denom
#Check proper or improper 
if denom>num:
    print (f"{num}/{denom}Fraction is propper")
    #use if and gcd to figure out wether fraction can be reduced or not
    if gcd == 1:
        print ("This proper fraction cannot be reduced any further.")
    else: print (f"This proper fraction can be reduced to {numgcd}/{degcd}")
else: 
    gcdnumde = math.gcd(numgcd, degcd)
    print(f"{num}/{denom} is an improper fraction.")
    #using if to i dentify wether the improper fractions can be reduced further or not 
    if gcd == 1 and denom > 1:
        print (f"The improper fraction cannot be reduced any further.\nThe mixed number is {wholenum} and {numgcd-(wholenum*degcd)}/{degcd}")
    elif gcd == 1:
        print (f"The improper fraction cannot be reduced any further.\nThe whole number is {wholenum}")
    elif gcdnumde == 1 and degcd > 1:
        print(f"The improper fraction can be reduced further to become: {numgcd}/{degcd}\nThe mixed number is {wholenum} and {numgcd - (wholenum * degcd)}/{degcd}")
    else: 
        print(f"The improper fraction can be reduced further to become: {numgcd}/{degcd}\nThe whole number is {wholenum}")