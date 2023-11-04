#ifndef RAILFENCE_H_
#define RAILFENCE_H_

void RailFence_Encryption(char* plaintext, int textSize, char* ciphertext, int key);
void RailFence_Decryption(char* ciphertext, int textSize, char* plaintext, int key);

#endif // !RAILFENCE_H_
