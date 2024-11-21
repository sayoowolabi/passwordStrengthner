
import string
import random

def is_valid(userPassword) -> bool:
    """FUNCTION TO CHECK IF THE PASSWORD MEETS CRITERIA"""
    
    cleared = True
    i = 0
    j = 0
    k = 0
    
    if len(userPassword) < 10:
        print("Password too weak")

        return False
    
    else:
        for char in userPassword:
            for i in range(0, len(string.digits)):
                if char == string.digits[i]:
                    checkNumbers = True
                else:
                    checkNumbers = False
                    
                    
        for char in userPassword:
            for j in range(0, len(string.punctuation)):
                if char == string.punctuation[j]:
                    checkChars = True
                else: checkChars = False
        
        for char in userPassword:
            for k in range(0,len(string.ascii_uppercase)):
                if char == string.punctuation[k]:
                    checkUppers = True
                else: 
                    checkUppers = False

        
    if checkNumbers == True:
        if checkChars == True:
            if checkUppers == True:
                cleared = True
    
    if cleared == False:
        print("Password too weak")
        return False
    else:
        return True



def strenghthen_password(password) -> str:
    """FUNCTION TO STRENGTHEN PASSWORD"""
    i = 0
    j = 0
    k = 0
    
    modifycheck = is_valid(password)
     
    if modifycheck == False:
        if len(password) < 10:
            
            while len(password) < 10:
                password = password + random.choice(string.ascii_letters + string.digits)
                
        for char in password:
            for i in range(0, len(string.digits)):
                if char == string.digits[i]:
                    isThereDigits = True
                else:
                    isThereDigits = False
        if isThereDigits == False:
            pasword = password + random.choice(string.digits)
            
            
        for char in password:
            for k in range(0,len(string.ascii_uppercase)):
                if char == string.punctuation[k]:
                    isThereUppers = True
                else: 
                    isThereUppers = False
        if isThereUppers == False:
            pasword = password + random.choice(string.ascii_uppercase)
            
        
        for char in password:
            for j in range(0, len(string.punctuation)):
                if char == string.punctuation[j]:
                    isThereSC = True
                else: isThereSC = False
        if isThereSC == False:
            pasword = password + random.choice(string.punctuation)
            
        print("Your new password is: ", password)
    


#### MAIN ###
passcode = ""

while (passcode == "exit") == False:
    
    passcode = input("Type  exit  to end. Enter A Password: ")
    if (passcode == "exit") == False:
    
        is_valid(passcode)
        newcode = strenghthen_password(passcode)
    
