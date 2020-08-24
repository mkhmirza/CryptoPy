#!/usr/bin/python env 

import getopt
import sys
from crypto import  Cryptography

def usage():
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> [OPTIONS...]")
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> [OPTIONS...] -k -v")
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> [OPTIONS...] -k -o <outputfile(without extension)>")
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> [OPTIONS...] -f <keyfilename(with extension)>")
    print(f"usage: {sys.argv[0]} -i <input-filename(with extension)> [OPTIONS...] -f <keyfilename(with extension)> -o <outputfile(without extension)>")
    print()

    print("options: ")
    print("-h,   prints this usage and exits")
    print("-e,   encryption operation to be performed")
    print("-d,   decryption operation to be performed") 
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

# encryption and decryption option given 
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

getOptions = [x[0] for x in opts]
# raise error if options -e and -d are used together 
if '-e' in getOptions and '-d' in getOptions:
    print("Options '-e' and '-d' cannot be used together")
    usage()
    sys.exit()

# raise error if options -e and -d are used together 
if '-k' in getOptions and '-f' in getOptions:
    print("Options '-k' and '-f' cannot be used together")
    usage()
    sys.exit()

# decryption can only be done by existing key file
if '-f' in getOptions and '-d' in getOptions:
    print("Options '-e' and '-d' cannot be used together")
    print("Decryption can only be done by existing key file.")
    usage()
    sys.exit()

# -k -> generate random key
# -f -> specify existing keyfile
# -i -> specify input file  
# no options were given || no -k or -f opts were given || no -i opts were given 
if len(opts) == 0 or inputfile == None or keyfile == None:
    usage()
    sys.exit(2)

crypto = Cryptography()

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
        print(f"Keyfile: {keyfile}")
   
    # encyption option without output filename
    if encryption == True:
        crypto.encryption(key, inputfile)
   
    # decryption option without output filename
    elif decryption == True:
        crypto.decryption(key, inputfile)

# output file was given
else:
    if verbose:
        print(f"Keyfile: {keyfile}")
        print(f"Outputfile: {outputfile}")
    # encyption option with output file
    if encryption == True:
        crypto.encryption(key, inputfile, outputfile)
   
    # decryption option with output file 
    elif decryption == True:
        crypto.decryption(key, inputfile, outputfile)



