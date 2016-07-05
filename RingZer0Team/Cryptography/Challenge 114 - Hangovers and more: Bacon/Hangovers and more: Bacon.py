"""
this text contains upper and lower case characters so it's encrypted with Baconian(something like morse code but with letters).
simply we can use this python code to convert it to a text that could decrypt with an Baconian cipher:
"""
message = "VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe d'ArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe n'est limIteE qUe par LE nombre DE cAlOries qU'ils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!VoiCI unE SUpeRbe reCeTtE cONcontee pAR un GrouPe d'ArtistEs culinaiRe, dONT le BOn Gout et lE SeNs de LA cLasSe n'est limIteE qUe par LE nombre DE cAlOries qU'ils PeUVEnt Ingurgiter. Ces virtuoses de la friteuse vous presente ce petit clip plein de gout savoureux !!"

encryptedM = ''

for i in range(len(message)):
    if message[i].isupper():
        encryptedM += 'B'
    if message[i].islower():
        encryptedM += 'A'

print encryptedM
"""
now use a Baconian cipher(like http://rumkin.com/tools/cipher/baconian.php) to decrypt it
"""
