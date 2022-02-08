hex_string1 = '1c0111001f010100061a024b53535009181c'
hex_string2 = '686974207468652062756c6c277320657965'

byte_array1 = bytes.fromhex(hex_string1)
byte_array2 = bytes.fromhex(hex_string2)

res = bytes(x ^ y for (x,y) in zip(byte_array1, byte_array2)).hex()

print(res)
