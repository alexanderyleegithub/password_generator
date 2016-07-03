#Version 1.2
#Alexander Lee
#User sets the # of characters and this generates a password 
#the password will have at least 1 char from lowercase, uppercase, number, and symbol 

import random
import string



#This is a function to formulate the password with at least 1 char of each
def finalpassword(length):
	#Lines 15-22 ensures at least 1 of each will be in the password
	print "You have chosen a length of %s characters" %length
	lowercase1 = string.ascii_lowercase
	atleast1lowercase = "".join((random.choice(lowercase1)) for x in range(1))
	uppercase1 = string.ascii_uppercase
	atleast1uppercase = "".join((random.choice(uppercase1)) for x in range(1))
	digits1 = string.digits
	atleast1digit = "".join((random.choice(digits1)) for x in range(1))
	symbols1 = "!@#$%^&+"
	atleast1symbol = "".join((random.choice(symbols1)) for x in range(1))

	atleast1ofeach = atleast1lowercase + atleast1uppercase + atleast1digit + atleast1symbol
	atleast1ofeachlist = list(atleast1lowercase) + list(atleast1uppercase) + list(atleast1digit) + list(atleast1symbol)
	random.shuffle(atleast1ofeachlist) #shuffles it so it will not follow the same pattern of lowercase+uppercase+digit+symbol
	#print atleast1ofeachlist --> this is in array form
	#print "".join(atleast1ofeachlist) # --> turns array into a combined string

	remaininglength = int(length) - 4
	if int(length) > 4:
	    possiblechars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&+"
	    remainingchars = "".join((random.choice(possiblechars)) for x in range(remaininglength))
	    finalpassword = "".join(atleast1ofeachlist) + remainingchars
	    print "This is your password %s" %finalpassword
	else:
	    print "This is your password %s" %"".join(atleast1ofeachlist)

# need to shuffle initial 4 characters

	
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
        
            elif int(passwordlength) >= 4:
                finalpassword(passwordlength)

    else:
	    print "not a digit, please try again"
