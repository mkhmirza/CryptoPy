#!/usr/bin/python env

from cryptography.fernet import Fernet
import sys

class Cryptography(object):
    def __init__(self):
        pass

    def encryption(self, keyName, inputfile, output='result'):
        """ 
        Encrypts data using python's Cryptography module
        keyName (str): key for encryption of data 
        output (str): output file name of ecrypted data
        (if no args are not given default is 'result.encrypted') 
        """
        
        try:
            # add extension to the output file
            output = output +".encrypted" 
            # init fernet class using key file given as a arg
            f = Fernet(keyName)
            
            # read the data to encrypt from input file 
            with open(inputfile, 'r') as file:
                data = file.readlines()
            
            # removing newline and encoding
            encoded = []
            for i in range(0, len(data)):
                data[i] = data[i].strip('\n')
                encoded.append(data[i].encode())
            
            # encrypting each ecoded line and writing it to a file
            token = []
            for i in encoded:
                token.append(f.encrypt(i))
            print(data)
            with open(output, 'w') as f:
                for tok in token:
                    f.writelines(tok.decode())
                    f.writelines("\n")
        except:
            print("There was an error.")
            print("--------------------------------------")
            print(f"Error: {sys.exc_info()[0]}")

    def generateKey(self, keyfileName='key.key'):
        """
        Generates a random key for encyption and decryption
        keyfileName (str): write the generated key and save as this file name
        """
        # generate a random key using fernet class 
        key = Fernet.generate_key()
        # write the generated key into a file and save it
        with open(keyfileName, 'wb') as file:
            file.write(key)
        return keyfileName 

    def decryption(self, keyName, inputfile, output="result"):
        """
        Decrypts data using python's Cryptography module
        keyName (str): key for decryption of data 
        output (str): output file name of decrypted data
        (if no args are not given default is 'result.txt') 
        """
        
        try: 
            # add extension to the output file
            output = output +".txt" 

            # init fernet class using key file given as a arg
            f = Fernet(keyName)

            # read the encypted from encrypted file  
            with open(inputfile,'rb') as file:
                data = file.readlines()

            token = []
            for i in range(0, len(data)):
                # data[i] = data[i].decode()
                # data[i] = data[i].strip('\n')
                token.append(f.decrypt(data[i]))
            
            #  write the encypted data into the output file with txt file
            with open(output, 'w') as file:
                for i in token:
                    file.writelines((i.decode()).__str__())
                    file.writelines("\n")
        except:
            print("There was an error.")   
            print("--------------------------------------")
            print(f"Error: {sys.exc_info()[0]}")


