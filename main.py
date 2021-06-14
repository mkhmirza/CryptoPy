#!/usr/bin/python env 

import getopt
import sys
from crypto import Cryptography
import argparse

parser = argparse.ArgumentParser(description="Encrypt & Decrypt Files using different techniques")
parser.add_argument('-e', '--encrypt', help='encryption to be performed', action='store_true')
parser.add_argument('-d', '--decrypt', help="decryption operation to be performed", action='store_true')
parser.add_argument('-i','--input', help='specify input file (with extension)')
parser.add_argument('-k', '--key', help='generates a new keyfile', action='store_true')
parser.add_argument('-f', '--key-file', help='key file name')
parser.add_argument('-o', '--output', help='specify outputfilename (without extension)')
args = vars(parser.parse_args())

# encryption and decryption option given 
encrypt = args['encrypt']
decrypt = args['decrypt']

# init vars 
inputf = args['input']
outputf = args['output']
keyf = args['key']
keyFile = args['key_file']
verbose = args['verbose']

if encrypt and decrypt:
    raise Exception("Encryption and Decryption cannot be performed together.")

if encrypt and not keyf:
    raise Exception("For encrpytion generating random key is recommended")

if decrypt and not keyFile:
     raise Exception("For decrpytion key file is required")

crypto = Cryptography()

# if encryption option '-e' is given
if encrypt:
    print("Generating a random key file for encrypting data")
    key = crypto.generateKey()
    with open(key, "r") as f:
        key = f.read()
    print("Encrypting Data..")
    crypto.encryption(key, inputf)

# if decryption option '-d' is given
elif decrypt:
    print("Reading key for decrypting data")
    key = keyFile
    with open(key, 'r') as f:
        key = f.read()
    print("Decrypting Data..")
    crypto.decryption(key, inputf)



