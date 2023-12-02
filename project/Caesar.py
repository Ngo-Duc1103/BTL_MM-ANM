import os

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val + shift) % 99999
        encrypted_text += chr(new_ascii_val)
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val - shift) % 99999
        decrypted_text += chr(new_ascii_val)    
    return decrypted_text

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to the file
file_path = os.path.join(script_dir, 'input.txt')

# Now use file_path when opening the file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

shift = 12

encrypted = caesar_encrypt(text, shift)
# Write the encrypted text to a file
encrypted_file_path = os.path.join(script_dir, 'encrypted.txt')
with open(encrypted_file_path, 'w', encoding='utf-8') as file:
    file.write(encrypted)
print(f"Encrypted text written to file at {os.path.abspath(encrypted_file_path)}")

decrypted = caesar_decrypt(encrypted, shift)
# Write the decrypted text to a file
decrypted_file_path = os.path.join(script_dir, 'decrypted.txt')
with open(decrypted_file_path, 'w', encoding='utf-8') as file:
    file.write(decrypted)
print(f"Decrypted text written to file at {os.path.abspath(decrypted_file_path)}")

# Compare the original text and the decrypted text
if text == decrypted:
    print("The plain text and the decrypted text is as same as each other. The algorithm works successfully.")
else:
    print("The plain text and the decrypted text is different compared to each other. The algorithm works unsuccessfully.")
