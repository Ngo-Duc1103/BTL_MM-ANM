def rail_fence_encrypt(text, num_rails):
    text = text.replace(' ', '')  # Remove spaces from the input text
    rails = [[] for _ in range(num_rails)]
    rail_idx, direction = 0, 1

    for char in text:
        rails[rail_idx].append(char)
        if rail_idx == 0:
            direction = 1
        elif rail_idx == num_rails - 1:
            direction = -1
        rail_idx += direction

    encrypted_text = ''.join([''.join(rail) for rail in rails])
    return encrypted_text

def rail_fence_decrypt(encrypted_text, num_rails):
    rails = [[] for _ in range(num_rails)]
    rail_lengths = [0] * num_rails
    rail_idx, direction = 0, 1

    for _ in encrypted_text:
        rail_lengths[rail_idx] += 1
        if rail_idx == 0:
            direction = 1
        elif rail_idx == num_rails - 1:
            direction = -1
        rail_idx += direction

    i = 0
    for rail in range(num_rails):
        for _ in range(rail_lengths[rail]):
            rails[rail].append(encrypted_text[i])
            i += 1

    decrypted_text = ""
    rail_idx, direction = 0, 1
    for _ in encrypted_text:
        decrypted_text += rails[rail_idx].pop(0)
        if rail_idx == 0:
            direction = 1
        elif rail_idx == num_rails - 1:
            direction = -1
        rail_idx += direction

    return decrypted_text

# Test the functions
text = "Thank you very much"
num_rails = 3

encrypted = rail_fence_encrypt(text, num_rails)
print(f"Encrypted: {encrypted}")

decrypted = rail_fence_decrypt(encrypted, num_rails)
print(f"Decrypted: {decrypted}")
