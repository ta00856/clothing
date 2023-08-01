import os
import binascii

def generate_secret_key():
    return binascii.hexlify(os.urandom(24)).decode()

print(generate_secret_key())
