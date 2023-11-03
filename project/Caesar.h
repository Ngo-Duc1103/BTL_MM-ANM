#ifndef CAESAR_H_
#define CAESAR_H_
#include <string.h>
#include <vector>

void Caesar_Encryption(char* plaintext, int textSize, char* ciphertext, int key);
void Caesar_Decryption(char* ciphertext, int textSize, char* plaintext, int key);

#endif // !CAESAR_H_
