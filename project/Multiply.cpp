#include "Multiply.h"
#include "Caesar.h"
#include "RailFence.h"

void Multiply_Encryption(char* plaintext, int textSize, char* ciphertext, int key){
	char* bridge = new char[textSize];

	int keyLoop = textSize % key;								// need a solution when keyLoop = 0 (which means no cipher)

	for (int i = 0; i < keyLoop; i++){
		Caesar_Encryption(plaintext, textSize, bridge, key);
		RailFence_Encryption(bridge, textSize, ciphertext, key);
	}

	delete [] bridge;
}

void Multiply_Decryption(char* ciphertext, int textSize, char* plaintext, int key){
	char* bridge = new char[textSize];

	int keyLoop = textSize % key;

	for (int i = 0; i < keyLoop; i++){
		RailFence_Decryption(bridge, textSize, ciphertext, key);
		Caesar_Decryption(plaintext, textSize, bridge, key);
	}

	delete [] bridge;
}