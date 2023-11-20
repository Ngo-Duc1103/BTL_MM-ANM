#include "Caesar.h"
// ----------------------------------------------------------------------------------
#include <iostream>
#include <string>

void Caesar_Encryption(std::string plaintext, int key, std::string& ciphertext);
void Caesar_Decryption(std::string ciphertext, int key, std::string& plaintext);

int main()
{
    std::string plaintext = u8"Hi, my name is Viet Bach! +-- '';';;;**&*&^&. ѠЄ Σ ǽ˷œŐ";
    int key = 3;
    std::string ciphertext;
    std::string decryptedtext;

    Caesar_Encryption(plaintext, key, ciphertext);
    Caesar_Decryption(ciphertext, key, decryptedtext);

    std::cout << "Plaintext: " << plaintext << std::endl;
    std::cout << "Ciphertext: " << ciphertext << std::endl;
    std::cout << "Decrypted text: " << decryptedtext << std::endl;

    if (plaintext == decryptedtext)
        std::cout << "Encryption and decryption successful!" << std::endl;
    else
        std::cout << "Encryption and decryption failed!" << std::endl;

    return 0;
}

void Caesar_Encryption(std::string plaintext, int key, std::string& ciphertext)
{
    std::string cipher;                                                        
    for (int i = 0; i < plaintext.size(); i++){
        char c = plaintext[i];
        if (c & 0x80) { // non-ASCII character
            cipher += char((c + key) % 256);
        } else if (isalpha(c)){
            if (islower(c))
                cipher += char(int(c + key - 97) % 26 + 97);
            else
                cipher += char(int(c + key - 65) % 26 + 65);
        }
		else if (c >= 32 && c <= 126){ // ASCII printable characters
			cipher += char((c - 32 + key) % 95 + 32);
		}
        else
            cipher += c;
    }
    ciphertext = cipher;
}

// Since this cipher is symmetric, decryption is technically reversed of encryption

void Caesar_Decryption(std::string ciphertext, int key, std::string& plaintext)
{
    std::string plain;
    for (int i = 0; i < ciphertext.size(); i++){
        char c = ciphertext[i];
        if (c & 0x80) { // non-ASCII character
            plain += char((c - key) % 256);
        } else if (isalpha(c)){
            if (islower(c))
                plain += char(int(c - key - 97 + 26) % 26 + 97);
            else
                plain += char(int(c - key - 65 + 26) % 26 + 65);
        }
		else if (c >= 32 && c <= 126){ // ASCII printable characters
			plain += char((c - 32 - key + 95) % 95 + 32);
		}
        else
            plain += c;
    }
    plaintext = plain;
}

// ----------------------------------------------------------------------------------
