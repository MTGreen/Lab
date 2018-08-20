# Program to Encrypt and Decrypt using CAESAR Shift Ciphers
import os
import string
import time
def Encrypt():
    print '''

    ################################
    Enter the Value of the Key     #
                                   #
                                   #
    ################################
    '''
    KEY = raw_input()
    print '''

    #########################################
    Enter the plain text that is required to#
    be encrypted                            #
                                            #
    #########################################
    '''
    plain = raw_input()
    #### Assigning Numbers to Alphabets #####
    ct, al = [], [] # ct is count and al is alphabet
    for x in range(0, 26):
        ct.append(x)
    for x in string.ascii_uppercase:
        al.append(x)
    scmap = dict(zip(ct, al))
    print'''

    #########################################
    #The dict of alphabet mapping to numbers#
    #########################################
    '''
    print scmap
    ### generating Cipher Text
    cipher = ""
    for x in plain.upper():
        if x.isalpha():
            new = int(KEY) + int(list(scmap.keys())[list(scmap.values()).index(x)])
            if new >25:
                new1 = new%26
                cipher+=scmap[new1]
            else:
                cipher+=scmap[new]
        else:
            cipher+=str(x)
    print '''
    ##################################
    #Cipher Text of the Plain Text is#
    ##################################
    '''
    print cipher
def Decrypt():
    print '''
    #########################################
    Enter the cipher text that is required  #
    to be decrypted                         #
                                            #
    #########################################
    '''
    cipher = raw_input()
    #### Assigning Numbers to Alphabets #####
    ct, al = [], []  # ct is count and al is alphabet
    for x in range(0, 26):
        ct.append(x)
    for x in string.ascii_uppercase:
        al.append(x)
    scmap = dict(zip(ct, al))
    print'''
       #########################################
       #The dict of alphabet mapping to numbers#
       #########################################
       '''
    print scmap
    ### Decrypting the Cipher Text
    for key in range(0,26):
        Start = time.time()
        plain = ""
        for x in cipher.upper():
            if x.isalpha():
                new = int(list(scmap.keys())[list(scmap.values()).index(x)]) - int(key)
                if new < 0:
                    new1 = new % 26
                    plain += scmap[new1]
                else:
                    plain += scmap[new]
            else:
                plain += str(x)
        print '''
        ###########################################
        # Key and Plain Text of the Cipher Text is#
        ###########################################
        '''
        print "Key :", key
        print "Time Taken in Seconds :", float(time.time() - Start)
        print plain
def main():
	print '''    
	Are you Encrypting or Decrypting using Brute Force
	Enter E for Encryption or D for Decryption
	
	'''
	choice = raw_input()
	print choice.upper()
	if choice.upper() == "E":
		Encrypt()
	elif choice.upper() == "D":
		Decrypt()
	elif choice.upper()!= 'E' or choice.upper() != 'D':
		print "Invalid Choice. Make Your Choice Correctly and Rerun the program"
main()
