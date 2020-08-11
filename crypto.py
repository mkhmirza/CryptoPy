#!/usr/bin/python env

from cryptography.fernet import Fernet

class Cryptography(object):
    def __init__(self,fileName):
        self.fileName = fileName

    def encryptData(self, keyName):
        """ Encrypts Data using Fernet class """
        
        f = Fernet(keyName)
        with open(self.fileName, 'r') as file:
            data = file.read()

        encodedData = data.encode()
        token = f.encrypt(encodedData)

        newFileName = self.fileName + ".encrypted"

        self.outputFile(token, newFileName)
    
    def outputFile(self, data, outputFileName):
        with open(outputFileName, 'wb') as file:
            file.write(data)

    def generateKey(self):
        key = Fernet.generate_key()
        with open("key.key",'wb') as file:
            file.write(key)
        return key

    def decryptData(self, keyName):

        f = Fernet(keyName)
        encryptedFileName = self.fileName  + ".encrypted"
        with open(encryptedFileName,'rb') as file:
            data = file.read()

        token = f.decrypt(data)

        outputFile = self.fileName
        self.outputFile(token, outputFile)


if __name__ == "__main__":
    fileName = "imp"
    crypto = Cryptography(fileName)
    key = crypto.generateKey()
    crypto.encryptData(key)
    crypto.decryptData(key)




