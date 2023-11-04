#include "RailFence.h"

void RailFence_Encryption(char* plaintext, int textSize, char* ciphertext, int key){
	// creating a temporary unblanked rail
    char** rail = new char*[key];                               // creating rows of rail

    for (int i = 0; i < key; i++) rail[i] = new char[textSize]; // creating columns of rail
 
    for (int i=0; i < key; i++)                                 // fully filling the rail for later use
        for (int j = 0; j < textSize; j++) rail[i][j] = '\n';
 
    // fill plaintext into rail
    bool falseUp_trueDown = false;
    int row = 0, col = 0;
 
    for (int i = 0; i < textSize; i++){
        if (row == 0 || row == key-1)                           // if it reaches 1st row, go down
            falseUp_trueDown = !falseUp_trueDown;               // if it reaches last row, go up
 
        rail[row][col++] = plaintext[i];                        // fill plaintext in rail diagonally
 
        falseUp_trueDown ? row++ : row--;
    }
 
    //  return ciphertext
    for (int i = 0; i < key; i++)
        for (int j = 0; j < textSize; j++)
            if (rail[i][j] != '\n') ciphertext[i] = rail[i][j];
 
    // delete rail
    for (int i = 0; i < key; i++) delete [] rail[i];
    delete [] rail;
}

void RailFence_Decryption(char* ciphertext, int textSize, char* plaintext, int key){
    
}
