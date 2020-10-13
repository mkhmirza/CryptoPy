# CryptoPy
Cryptopy is a command line based python application which can be used for encrpyting and decrypting different files. The application uses python's cryptography module which is referenced below in the documentation section.

## Usage 
### General Usage
usage: `main.py -i <input-filename(with extension)> [OPTIONS...]`
#### Information
usage: `main.py -h`
### Encryption 
1. `main.py -i <input-filename(with extension)> -e -k -v`
2. `main.py -i <input-filename(with extension)> -e -k -o <outputfile(without extension)>`
3. `main.py -i <input-filename(with extension)> -e -f <keyfilename(with extension)>`
4. `main.py -i <input-filename(with extension)> -e -f <keyfilename(with extension)> -o <outputfile(without extension)>`
### Decryption
1. `main.py -i <input-filename(with extension)> -d -f <keyfilename(with extension)> -v`
2. `main.py -i <input-filename(with extension)> -d -f <keyfilename(with extension)> -o <outputfile(without extension)>`    


## Documentation 
Documentation of Cryptography Library can be viewed at [Cryptography Library Python](https://cryptography.io/en/latest/)


