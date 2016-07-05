"""
If we decrypt it with base64, it gives us "EOBD.7igq4;1ikb51ibOO0;:41R". 'E' ^ 'F' = 3 so we should XOR each character with 3 to reach the flag.
code below does the hole thing and gives the flag :)
"""
import base64

challenge = 'RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS'
decrypted = base64.b64decode(challenge)
flag = ''.join(chr(ord(i) ^ 3) for i in decrypted)
print(flag)

#so the flag is: FLAG-4jdr782jha62jaLL38972Q
