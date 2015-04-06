#basic encryption using base64

#import modules base64 to encrypt and getpass to get password without echo
import base64
import getpass

CoD= raw_input ("Desea cifrar (c) o descifrar (d) el pwd? c/d:")
if CoD == "c":
    password = getpass.getpass('Digite el password a cifrar:')
    cifrado= base64.b64encode(password)
    print ("El password cifrado es: "+cifrado)
    exit   
else:
    password= raw_input ("Ingrese el password cifrado: ")
    decrypt= base64.b64decode(password)
    print ("El password es: "+decrypt)
    exit