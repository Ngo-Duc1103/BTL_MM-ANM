

#include <iostream>
#include "Caesar.h"
#include "RailFence.h"
#include "Multiply.h"

int main()
{
	char plaintext[] = "";
	char* ciphertext = new char[100]; //Đây chỉ là tạo tạm thời, mọi người có thể tự tạo biến của mình
	char key[] = "";
	
	CaesarEncrypt(plaintext, ciphertext, key);
	RailFenceEncrypt(plaintext, ciphertext, key);
	MultiplyEncrypt(plaintext, ciphertext, key);
}

