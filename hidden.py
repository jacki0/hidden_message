import hashlib
import string


alphabet = ''.join([chr(i) for i in range(ord('а'), ord('а') + 34)])
alphabet = alphabet[: 6] + alphabet[-1] + alphabet[6: -2]
alphabet += string.digits + string.ascii_letters + ' ' + string.punctuation + alphabet.upper()
alphabet *= 3


def keygen(message):
    key = hashlib.sha256(bytes(message, 'utf-8')).hexdigest()
    return key


def encrypt(message, key):
    cryptmessage = ''
    for letter in message:
        i = (alphabet.find(letter) + key) * 2
        cryptmessage += alphabet[i]
    return cryptmessage


def decrypt(cryptmessage, key):
    message = ''
    for letter in cryptmessage:
        i = alphabet.find(letter)
        if i % 2 != 0: 
            i += 161
        message += alphabet[(i // 2) - key]
    return message
