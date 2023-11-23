def multiplicative_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val * key) % 99999
        encrypted_text += chr(new_ascii_val)
    return encrypted_text

def multiplicative_decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        ascii_val = ord(char)
        # Find multiplicative inverse
        multiplicative_inverse = pow(key, -1, 99999)
        new_ascii_val = (ascii_val * multiplicative_inverse) % 99999
        decrypted_text += chr(new_ascii_val)
    return decrypted_text

# Test the functions
text = "Hello, World! @@@"
key = 82000

print(f"Plaintext: {text}")

encrypted = multiplicative_encrypt(text, key)
print(f"Encrypted: {encrypted}")

decrypted = multiplicative_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
