# Check the validity of the input
def checkDecimal(number):
    for i in number:
        if i not in {'0','1','2','3','4','5','6','7','8','9'}:
            return False
    return True
def checkBinary(number):
    for i in number:
        if i not in {'0','1'}:
            return False
    return True
def checkOctal(number):
    for i in number:
        if i not in {'0','1','2','3','4','5','6','7'}:
            return False
    return True
def checkHexa(number):
    for i in number:
        if(i not in {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}):
            return False
    return True
# Converting Functions
def decimalToBinary(number): #Function converts from decimal to binary
    binary=''
    num=int(number)
    while num>0:
        reminder =num%2
        binary = str(reminder)+binary
        num//=2
    return binary
def decimalToOctal(number): #Function converts from decimal to octal
    octal=''
    num=int(number)
    while num>0:
        reminder = num%8
        octal = str(reminder)+octal
        num//=8
    return octal
def decimalToHexa(number): #Function converts from decimal to hexadecimal
    hexa=''
    num=int(number)
    hexaMap1={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while num>0:
        reminder = num%16
        if(reminder>=10):
            hexa = hexaMap1[reminder]+hexa
        elif(reminder<10):
            hexa = str(reminder)+hexa
        num //=16
    return hexa
def binaryToDecimal(number): #Function converts from binary to decimal
    decimal=0
    power=0
    for digit in reversed(number):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal
def octalToDecimal(number): #Function converts from octal to decimal
    decimal = 0
    power = 0
    for digit in reversed(number):
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal
def hexaToDecimal(number): #Function converts from hexadecimal to decimal
    decimal = 0
    power = 0
    hexmap2 = {'A': 10,'B': 11,'C': 12,'D': 13,'E': 14,'F': 15}
    for digit in reversed(number):
        if digit in hexmap2:
            decimal += hexmap2[digit]*(16 ** power)
        else:
            decimal += int(digit)*(16 ** power)
        power += 1
    return decimal
#The Main Functions
def main():
        while True:
            print("*Numbering system converter*")
            choice1=(input("A) Insert a new number\nB) Exit program\nYour choice: ")) #Displaying the first menu
            if (choice1 =='A'):
                number = input("Please insert a number: ").upper()
                baseFrom(number) #Calling baseFrom function
            elif(choice1=='B'):
                print("Exiting program!")
                break
            else:
                print("\nPlease select a valid choice")
def baseFrom(number): #Function to know what is the base of the inserted number
    while True:
        print("\n*Please select the base you want to convert a number from*")
        menu1 = input("A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\nYour choice: ") #Displaying the second menu
        if menu1 in ['A','B','C','D']:
            baseTo(number,menu1) #Calling baseTo function
            break
        else: 
            print("\nPlease select a valid\n")
def baseTo(number,menu1): #Function to take the base the number will be converted to
    while True:
        print("\n*Please select the base you want to convert a number to*")
        menu2 = input("A) Decimal\nB) Binary\nC) Octal\nD) Hexadecimal\nYour choice: ") #Displaying the third menu
        if menu2 in ['A','B','C','D']:
            converted=convertNumber(number,menu1,menu2)
            if (converted != 0): #If 0 the number the user entered is not valid for execute the operation
                print(converted,"\n") #Displaying number after convertion
                break
            else:
                break
        else:
            print("\nPlease select a valid choice")
def convertNumber(number,menu1,menu2): #Function where the convertion occures
        if(menu1=='A'):
            if(checkDecimal(number)):
                if(menu2=='A'):
                    return number
                elif(menu2=='B'): #Converting from decimal to binary
                    result=decimalToBinary(number) 
                    return result
                elif(menu2=='C'): #Converting from decimal to octal
                    result=decimalToBinary(number)
                    return result
                elif(menu2=='D'): #Converting from decimal to hexadecimal
                    result=decimalToHexa(number)
                    return result
            else:
                print("The number you entered is not a valid decimal number.\n")
                return 0
        elif(menu1=='B'):
            if(checkBinary(number)):
                if(menu2=='A'): #Converting from binary to decimal
                    result=binaryToDecimal(number)
                    return result
                elif(menu2=='B'):
                    return number
                elif(menu2=='C'): #Converting from binary to octal
                    decimal=binaryToDecimal(number)
                    result=decimalToOctal(decimal)
                    return result
                elif(menu2=='D'): #Converting from binary to hexadecimal
                    decimal=binaryToDecimal(number)
                    result=decimalToHexa(decimal)
                    return result
            else: 
                print("The number you entered is not a valid binary number.\n")
                return 0
        elif(menu1=='C'):
            if(checkOctal(number)):
                if(menu2=='A'): #Converting from octal to decimal
                    result=octalToDecimal(number)
                    return result
                elif(menu2=='B'): #Converting from octal to binary
                    decimal=octalToDecimal(number)
                    result=decimalToBinary(decimal)
                    return result
                elif(menu2=='C'):
                    return number
                elif(menu2=='D'): #Converting from octal to hexadecimal
                    decimal=octalToDecimal(number)
                    result=decimalToHexa(decimal)
                    return result
            else:
                print("The number you entered is not a valid octal number.\n")
                return 0
        elif(menu1=='D'):
            if(checkHexa(number)):
                if(menu2=='A'): #Converting from hexadecimal to decimal
                    result=hexaToDecimal(number)
                    return result
                elif(menu2=='B'): #Converting from hexadecimal to binary
                    decimal=hexaToDecimal(number)
                    result=decimalToBinary(decimal)
                    return result
                elif(menu2=='C'): #Converting from hexadecimal to octal
                    decimal=hexaToDecimal(number)
                    result=decimalToOctal(decimal)
                    return result
                elif(menu2=='D'):
                    return number
            else: 
                print("The number you entered is not a valid hexadecimal number.\n")
                return 0
            
main() #Calling the main function to start the program