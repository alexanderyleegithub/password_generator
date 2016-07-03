#Version 1.3
#https://github.com/alexanderyleegithub
#Alexander Lee
#User sets the # of characters and this generates a password 
#the password will have at least 1 char from lowercase, uppercase, number, and symbol 

import random
import string



#This is a function to formulate the password with at least 1 char of each
def finalpassword(length):
	#Lines 15-23 ensures at least 1 of each will be in the password
	print "You have chosen a length of %s characters" %length
	lowercase1 = string.ascii_lowercase
	atleast1lowercase = "".join((random.choice(lowercase1)) for x in range(1))
	uppercase1 = string.ascii_uppercase
	atleast1uppercase = "".join((random.choice(uppercase1)) for x in range(1))
	digits1 = string.digits
	atleast1digit = "".join((random.choice(digits1)) for x in range(1))
	symbols1 = "!@#$%^&+"
	atleast1symbol = "".join((random.choice(symbols1)) for x in range(1))
    
    #lLines 26-27 turns the combined 4 into a list for shuffling
	atleast1ofeach = atleast1lowercase + atleast1uppercase + atleast1digit + atleast1symbol
	atleast1ofeachlist = list(atleast1lowercase) + list(atleast1uppercase) + list(atleast1digit) + list(atleast1symbol)
	#shuffles it so it will not follow the same pattern of lowercase+uppercase+digit+symbol of the initial 4 characters
	random.shuffle(atleast1ofeachlist) 
	
    #Lines 32-39 adds all remaining possible characters into the mix, then reshuffles it so the inital 4 will not consist of the same characters
	remaininglength = int(length) - 4
	if int(length) > 4:
	    possiblechars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&+" #all possible characters
	    remainingchars = "".join((random.choice(possiblechars)) for x in range(remaininglength)) #creates a string based on remaining length of chars 
	    finalpassword = (atleast1ofeachlist) + list(remainingchars) #puts all values as a list and into variable "finalpassword"
	    random.shuffle(finalpassword) #shuffles the "finalpassword" so the initial 4 will not have same characters
	    shuffledfinalpassword = "".join(finalpassword)
	    print "This is your password %s" %shuffledfinalpassword
	#Lines 41-43 prints the shuffled initial 4
	else:
	    print "This is your password %s" %"".join(atleast1ofeachlist)


#EXCESS CODE
#The following 3 lines shuffles a string by turning it into a list first
#lst = list('dog')
#random.shuffle(lst)
#print "".join(lst)
	   
#The following 3 lines shuffles a list   
#generatedpassword = [1,2,3,4,5]
#random.shuffle(generatedpassword)
#print generatedpassword

#print atleast1ofeachlist --> this is in array form
#print "".join(atleast1ofeachlist) # --> turns array into a combined string

print "Generate a random password based on 0-9,a-z,A-Z and random symbols"
while True:
    print "How long do you want your password? (at least 4 characters)"
    passwordlength = raw_input("> ")
    if passwordlength.isdigit(): #checks if its a digit so program will not crash
            if int(passwordlength) < 4:
		        print "less than 4, please try again"
        
            elif int(passwordlength) >= 4:
                finalpassword(passwordlength)

    else:
	    print "Not a digit, please try again"
