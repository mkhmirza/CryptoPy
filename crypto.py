#!/usr/bin/python env

from cryptography.fernet import Fernet

class Cryptography(object):
    def __init__(self,fileName):
        self.fileName = fileName

    def encryption(self, keyName, output='result'):
        """ 
        Encrypts data using python's Cryptography module
        keyName (str): key for encryption of data 
        output (str): output file name of ecrypted data
        (if no args are not given default is 'result.encrypted') 
        """
        
        try:
            # add extension to the output file
            output = output +".encypted" 

            # init fernet class using key file given as a arg
            f = Fernet(keyName)

            # read the data to encrypt from input file 
            with open(self.fileName, 'r') as file:
                data = file.read()

            # encoded data 
            encoded = data.encode()
            # returns data with encyption
            token = f.encrypt(encoded)

            # write the encypted data into the output file 
            with open(output, 'wb') as file:
                file.write(token)

        except:
            print("There was a error.")

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

    def decryptData(self, keyName):

        f = Fernet(keyName)
        encryptedFileName = self.fileName  + ".encrypted"
        with open(encryptedFileName,'rb') as file:
            data = file.read()

        token = f.decrypt(data)

        outputFile = self.fileName
        self.outputFile(token, outputFile)

