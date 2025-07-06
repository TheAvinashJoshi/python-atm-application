import os


def askForPIN(isTriedAgain=0):
    securityInformation = """Please note below points for security concerns
                            1. Please do not disclose your PIN to anybody
                            2. Make sure you hide your PIN while entering into application
                            3. Please do not exit without comfirming exit message"""
    # dont show the security information if user has already entered a PIN 
    # and now re entering
    if not isTriedAgain:
        print(securityInformation)
    return input("Please enter your secret PIN and press enter: ")    


def greetUser():
    print("Welcome to Python Bank")


def handleAfterLoginATMFunctions():
    os.system('cls')
    selectedOption = ""
    selectedOption = showOptions()
    if selectedOption == "1":
        os.system('cls')
        checkBalance()
    elif selectedOption == "2":
        os.system('cls')
        deposit()
        print(f"Updated Balance: {accountBalance}")
        handleGoBack()
    elif selectedOption == "3":
        os.system('cls')
        withdraw()
        print(f"Remaining Balance: {accountBalance}")
        handleGoBack()
    elif selectedOption == "0":
        exitFromApplication()
    else:
        print("Please enter valid option")
 

def exitFromApplication():
    os.system('cls')
    print("Thank you for banking with us, See you again")
    exit()


def handleGoBack():
    if input("Enter BACK to go back to Menu and EXIT to exit: ") == "BACK":
        handleAfterLoginATMFunctions()
    else:
        exitFromApplication()


def showOptions():  
    print("""Please enter action you want to perform
           1. Type 1 to check your balance
           2. Type 2 to deposit money
           3. Type 3 to withdraw money
           4. Type 0 to EXIT
          """)
    return input("Please type here and press enter: ")


def withdraw():
    global accountBalance, amountToWithdraw
    amountToWithdraw = input("Please enter the amount you want to withdraw: ")
    if float(amountToWithdraw) > float(accountBalance):
        print("Insufficient balance")
        withdraw()
    else:
        accountBalance -= float(amountToWithdraw)
    

def deposit():
    os.system('cls')
    global accountBalance, amountToDeposit
    amountToWithdraw = input("Please enter the amount you want to deposit: ")
    accountBalance += float(amountToWithdraw)


def checkBalance():
    os.system('cls')
    print(F"Your current balance is INR {accountBalance}")
    handleGoBack()


# main functionality starts here

os.system('cls')
accountBalance = 12350.80
greetUser()
pin = askForPIN()
pinFound = pin != None and len(str(pin).strip()) > 0
while not pinFound:
    print("The PIN you entered is invalid! ")
    pin = askForPIN(1)
    if len(str(pin).strip()) > 0:
        break


handleAfterLoginATMFunctions()