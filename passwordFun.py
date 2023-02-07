def isValidPassword(password):
    
    if(len(password)>=10) :
        lowerCase = False
        lcCount = 0
        uppercase = False
        ucCount = 0
        num = False
        special = False
        scCount = 0
        
        for char in password:
            if(char.isdigit()) :
                num = True
            if char.islower():
                lcCount += 1
                if lcCount >=2 :
                 lowerCase = True
            if char.isupper():
                ucCount += 1
                if ucCount >=2:
                 uppercase = True
            if not char.isalnum():
                scCount += 1
                if scCount>=3:
                 special = True
        return lowerCase and uppercase and num and special
    else :
        return False
    
password1 = input(" Enter your password  ")
print(isValidPassword(password1))








        
            


        
      
    
