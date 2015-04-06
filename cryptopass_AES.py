#encryption using AES
#v1 based on http://fearoflightning.blogspot.com/2012/01/pycrypto-text-encryption.html

from Crypto.Cipher import AES
import base64
import getpass

PADDING = '{'
BLOCK_SIZE = 32
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#prepare crypto method
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

CoD= raw_input ("Desea cifrar (c) o descifrar (d) el pwd? c/d:")
key= raw_input("Ingrese la llave de cifrado - 16 caracteres:")
crypKey= AES.new(key)

if CoD == "c":
    if len(key)==16:
        #iv = Random.new().read(AES.block_size)
        password = getpass.getpass('Digite el password a cifrar:')
        cifrado= EncodeAES(crypKey, password)
        print cifrado 
        exit
    else: 
        key= raw_input("Ingrese la llave de cifrado - 16 caracteres, la anterior fue de "+str(len(key))+" caracteres:")
else:
    if len(key)==16:
        password= raw_input ("Digite el password cifrado:")
        deco = DecodeAES(crypKey, password)
        print deco 
        exit