def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val + shift) % 256
        encrypted_text += chr(new_ascii_val)
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val - shift) % 256
        decrypted_text += chr(new_ascii_val)
    return decrypted_text

# Test the functions
text = "Hello, World! @@@"
shift = 1314

print(f"Plaintext: {text}")

encrypted = caesar_encrypt(text, shift)
print(f"Encrypted: {encrypted}")

decrypted = caesar_decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")
