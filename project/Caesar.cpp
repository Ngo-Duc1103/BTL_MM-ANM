#include "Caesar.h"

// !!! THESE ARE ENCRYPTION AND DECRYPTION OF ONLY ENGLISH-BASED ALPHABETS, NOT UTF-8 STANDARD !!!

int modulo(int num){
    if (num >= 0) return num % 26;
    else{
        while (num < 0) num += 26;
        return num;
    }
}

void Caesar_Encryption(char* plaintext, int textSize, char* ciphertext, int key)
{
	std::vector<char> cipher;																// use vector cuz not know the size of plaintext
    for (int i = 0; i < textSize; i++){
        if (90 >= plaintext[i] && plaintext[i] >= 65)
			cipher.push_back( char( int( 65 + modulo(plaintext[i] + key - 65) ) ) );		// encrypt with capital letters
		else if (122 >= plaintext[i] && plaintext[i] >= 97)
			cipher.push_back( char( int( 97 + modulo(plaintext[i] + key - 97) ) ) );		// encrypt with non-capital letters
	}

	for (int i = 0; i < cipher.size(); i++) ciphertext[i] = cipher[i];						// move ciphertext from inner function to main
}


// Since this cipher is symmetric, decryption is technically reversed of encryption

void Caesar_Decryption(char* ciphertext, int textSize, char* plaintext, int key)
{
	std::vector<char> plain;
    for (int i = 0; i < textSize; i++){
        if (90 >= ciphertext[i] && ciphertext[i] >= 65)
			plain.push_back( char( int( 65 + modulo(ciphertext[i] - key - 65) ) ) );
		else if (122 >= ciphertext[i] && ciphertext[i] >= 97)
			plain.push_back( char( int( 97 + modulo(ciphertext[i] - key - 97) ) ) );
	}

	for (int i = 0; i < plain.size(); i++) plaintext[i] = plain[i];
}