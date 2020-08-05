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
        with open(outputFileName, 'w') as file:
            file.write(data.__str__())

    def generateKey(self):
        key = Fernet.generate_key()
        with open("key.key",'w') as file:
            file.write(key.__str__())
        return key


if __name__ == "__main__":
    fileName = "imp"
    crypto = Cryptography(fileName)
    key = crypto.generateKey()
    crypto.encryptData(key)





