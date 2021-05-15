#TypeCasting
import os
decision = True
while decision:
    num = int(input("Enter a number: "))
    os.system('cls')
    fact = 1 #Container for Final Value
    for z in range (num, 10, -1):

        fact *=z
    print("The answer is: ", fact)
    choice = input("Press [y] to continue or any key to exit: ")
    os.system('cls')
    decision = choice == "y" or choice == "Y"

