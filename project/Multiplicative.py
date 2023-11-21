def multiplicative_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1

def multiplicative_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val * key) % 256
        encrypted_text += chr(new_ascii_val)
    return encrypted_text

def multiplicative_decrypt(encrypted_text, key):
    decrypted_text = ""
    inverse_key = multiplicative_inverse(key, 256)
    if inverse_key == -1:
        return "Error: Key is not invertible"
    for char in encrypted_text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val * inverse_key) % 256
        decrypted_text += chr(new_ascii_val)
    return decrypted_text

# Test the functions
text = "Hello, World!"
key = 7

encrypted = multiplicative_encrypt(text, key)
print(f"Encrypted: {encrypted}")

decrypted = multiplicative_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
