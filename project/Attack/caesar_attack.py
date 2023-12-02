import os
import operator

# Caesar Encrypt
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val + shift) % 99999
        encrypted_text += chr(new_ascii_val)
    return encrypted_text

# Counting different Characters
def count_unique_characters(text): 
    return len(set(text))

# Frequency Analysis
def frequency_analysis(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    sorted_frequency = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)

    common_char_tab = sorted_frequency[:count_unique_characters(encrypted)]
    for char, freq in common_char_tab:
        print(f"Character: {char}, Frequency: {freq}, UTF-8 code: {ord(char)}")
    
    most_common_char = sorted_frequency[0][0]
    return most_common_char

# Caesar Attack
def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        ascii_val = ord(char)
        new_ascii_val = (ascii_val - shift) % 99999
        decrypted_text += chr(new_ascii_val)
    return decrypted_text

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))
# Construct the full path to the plaintext file
plaintext_file_path = os.path.join(script_dir, 'plaintext.txt')
# Now use plaintext_file_path when opening the file
with open(plaintext_file_path, 'r', encoding='utf-8') as file:
    plaintext = file.read()
print(f"Plaintext read from file at {os.path.abspath(plaintext_file_path)}")

shift = int(input("Enter a shift value: "))
encrypted = caesar_encrypt(plaintext, shift)
# Write the encrypted text to a file
encrypted_file_path = os.path.join(script_dir, 'encrypted.txt')
with open(encrypted_file_path, 'w', encoding='utf-8') as file:
    file.write(encrypted)
print(f"Encrypted text written to file at {os.path.abspath(encrypted_file_path)}")


#----------------------------Processing-----------------------------------------#
#--------------------------Decrypt with space-----------------------------------#
most_common_char = frequency_analysis(encrypted)
print(f"\n")
shift_space = ord(most_common_char) - ord(' ')
decrypted_space = caesar_decrypt(encrypted, shift_space)

# Write the decrypted text to a file
decrypted_file_path = os.path.join(script_dir, 'decrypted.txt')
with open(decrypted_file_path, 'w', encoding='utf-8') as file:
    file.write(f"Decrypted text with key {shift_space}:\n")
    file.write(decrypted_space)
    file.write("\n\n//-----------------------------------------------------------------------------//")
    file.write("\n\n")

# Compare the original text and the decrypted text
if plaintext == decrypted_space:
    print(f"The plaintext and the decrypted text in decrypted_space are the same. The algorithm works successfully with shift space. Key value is: {shift_space}")
else:
    print(f"The plaintext and the decrypted text in decrypted_space is different compared to each other. The algorithm works unsuccessfully with shift space. Key value is: {shift_space}")

#--------------------------Decrypt with char-----------------------------------#

common_chars_english = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd']

# Open the decrypted file in write mode
decrypted_file_path = os.path.join(script_dir, 'decrypted.txt')
with open(decrypted_file_path, 'a', encoding='utf-8') as file:
    # Write the decrypted text for each common character in English
    for char in common_chars_english:
        shift_char = ord(most_common_char) - ord(char)
        decrypted = caesar_decrypt(encrypted, shift_char)
        file.write(f"Decrypted text with key {shift_char}:\n")
        file.write(decrypted)
        file.write("\n\n//-----------------------------------------------------------------------------//")
        file.write("\n\n")

        if plaintext == decrypted:
            print(f"The plaintext and the decrypted text in 'decrypted_{char}.txt' are the same. The algorithm works successfully with shift {char}. Key value is {shift_char}")
        else:
            print(f"The plaintext and the decrypted text in 'decrypted_{char}.txt' are different. The algorithm works unsuccessfully with shift {char}. Key value is {shift_char}")
        
print(f"\nAll decrypted texts written to file at {os.path.abspath(decrypted_file_path)}")
