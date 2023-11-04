#ifndef MULTIPLY_H_
#define MULTIPLY_H_

void Multiply_Encryption(char* plaintext, int textSize, char* ciphertext, int key);
void Multiply_Decryption(char* ciphertext, int textSize, char* plaintext, int key);

#endif // !MULTIPLY_H_
