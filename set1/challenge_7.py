import base64
from Crypto.Cipher import AES

def decrypt_AES_ECB(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)

    plaintext = cipher.decrypt(ciphertext)

    return plaintext

ciphertext = base64.b64decode(open("7.txt").read())
plaintext = decrypt_AES_ECB(b'YELLOW SUBMARINE', ciphertext)

print(plaintext.decode("utf-8"))