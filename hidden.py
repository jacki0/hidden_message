import hashlib
import string

def keygen(message):
    key = hashlib.sha256(bytes(message, 'utf-8')).hexdigest()
    return key


def encrypt(message, key):
    cryptmessage = ''
    alphabet = ord('а')
    alphabet = ''.join([chr(i) for i in range(alphabet, alphabet + 6)] + [chr(alphabet + 33)] + [chr(i) for i in range(alphabet + 6, alphabet + 32)])
    alphabet += string.digits + string.ascii_letters + ' ' + string.punctuation + alphabet.upper()
    for letter in message:
        i = alphabet.find(letter) * key
        while i >= len(alphabet):
            i -= len(alphabet) - 1
        cryptmessage += alphabet[i]
    return cryptmessage
