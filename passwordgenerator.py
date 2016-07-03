#Version 1.0 
#Alexander Lee
#User sets the # of characters and this generates a password based on a string
#at least 1 char from lowercase, uppercase, number, and symbol 

import random
import sys
import string



#This is a function to formulate the characters from the password bank
def finalpassword(length):
    
	possiblechars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%"
	
	print "You have chosen a length of %s characters" %length
	print "".join((random.choice(possiblechars)) for x in range(int(length)))
	
	
	
#The following 3 lines shuffles a string
#lst = list('dog')
#random.shuffle(lst)
#print "".join(lst)
	   
#The following 3 lines shuffles a list   
#generatedpassword = [1,2,3,4,5]
#random.shuffle(generatedpassword)
#print generatedpassword


print "Generate a random password based on 0-9,a-z,A-Z and random symbols"
while True:
    print "How long do you want your password? (at least 4 characters)"
    passwordlength = raw_input("> ")
    if passwordlength.isdigit():
        if int(passwordlength) < 4:
		    print "less than 4, please try again"
            
        else:
		    print "Processing..."
        finalpassword(passwordlength)
    else:
	    print "not a digit"
 


