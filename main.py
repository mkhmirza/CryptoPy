#!/usr/bin/python env 

import getopt
import sys
from crypto import  Cryptography

def usage():
    print()
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> [OPTIONS...]")
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> -k -v")
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> -k -o <outputfile(without extension)>")
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> -f <keyfilename(with extension)>")
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> -f <keyfilename(with extension)> -o <outputfile(without extension)>")
    print()
    print("Options: ")
    print("-h,   prints out help and exits")
    print("-e,   encryption option")
    print("-d,   decryption option") 
    print("-i,   specify input file (with extension)")
    print("-k,   generates a new keyfile")
    print("-f    specify keyfilename (with extension)")
    print("-o,   specify outputfilename (without extension)")
    print("-v,   verbose option")
    print()


try:
    # get these options and arguments,
    # <a-z>i represents option without argument
    opts, args = getopt.getopt(sys.argv[1:], "hi:ei:di:i:ki:f:o:v")
    
except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)

encryption = False
decryption = False

# init vars 
inputfile = None
outputfile = None
keyfile = None
verbose = False

for opt, arg in opts:
    if opt == '-h':
        usage()
        sys.exit(2)
    elif opt == '-e':
        encryption = True
    elif opt == '-d':
        decryption = True
    elif opt == '-k':
        keyfile = True
    elif opt == '-i':
        inputfile = arg
    elif opt == '-o':
        outputfile = arg
    elif opt == '-f':
        keyfile = arg
    elif opt == '-v':
        verbose = True


# -k -> generate random key
# -f -> specify existing keyfile
# -i -> specify input file  
# no options were given || no -k or -f opts were given || no -i opts were given 
if len(opts) == 0 or inputfile == None or keyfile == None:
    usage()
    sys.exit(2)

crypto = Cryptography(inputfile)

# opts -k were given 
# if this is not true then meaning -f opts were given 
if keyfile == True:
    # verbose option is on
    if verbose:
        print("Generating random key for encryption and decrpytion...")
    # generating a new key file and returning the name of the file 
    keyfile = crypto.generateKey()

# read the given or generated key file 
with open(keyfile, 'r') as f:
    key = f.read()

# no output file was given
if outputfile == None:    
    if verbose:
        print("Encypting input file")
        print(f"Keyfile: {keyfile}")
    # encypt data using key and use default output filename
    crypto.encryption(key)
# output file was given
else:
    if verbose:
        print("Encypting input file")
        print(f"Keyfile: {keyfile}")
        print(f"Outputfile: {outputfile}")
    # encypt data using key and given output filename
    crypto.encryption(key, outputfile)



