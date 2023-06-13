﻿// ConsoleApplication2.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

char* enBase64(char* in, int len);
int main()
{
	char a[] = "ABC";
	char b[] = "ABCD";
	char c[] = "ABCDE";

	printf("%s\n",enBase64(a,3));
	printf("%s\n",enBase64(b,4));
	printf("%s\n", enBase64(c, 5));


	return 0;
}

char* enBase64(char* in, int len)
{

	char v3[85];
	char* v5;
	unsigned int v6;
	bool v7 = 0;
	bool v8 = 0;
	unsigned int v9;
	char* v10;
	unsigned int i;

	v3[0] = 'A';
	v3[1] = 66;
	v3[2] = 67;
	v3[3] = 68;
	v3[4] = 69;
	v3[5] = 70;
	v3[6] = 71;
	v3[7] = 72;
	v3[8] = 73;
	v3[9] = 74;
	v3[10] = 75;
	v3[11] = 76;
	v3[12] = 77;
	v3[13] = 78;
	v3[14] = 79;
	v3[15] = 80;
	v3[16] = 81;
	v3[17] = 82;
	v3[18] = 83;
	v3[19] = 84;
	v3[20] = 85;
	v3[21] = 86;
	v3[22] = 87;
	v3[23] = 88;
	v3[24] = 89;
	v3[25] = 90;
	v3[26] = 'a';
	v3[27] = 'b';
	v3[28] = 99;
	v3[29] = 100;
	v3[30] = 101;
	v3[31] = 102;
	v3[32] = 103;
	v3[33] = 104;
	v3[34] = 105;
	v3[35] = 106;
	v3[36] = 107;
	v3[37] = 108;
	v3[38] = 109;
	v3[39] = 110;
	v3[40] = 111;
	v3[41] = 112;
	v3[42] = 113;
	v3[43] = 114;
	v3[44] = 115;
	v3[45] = 116;
	v3[46] = 117;
	v3[47] = 118;
	v3[48] = 119;
	v3[49] = 'x';
	v3[50] = 'y';
	v3[51] = 'z';
	v3[52] = '0';
	v3[53] = '1';
	v3[54] = 50;
	v3[55] = 51;
	v3[56] = 52;
	v3[57] = 53;
	v3[58] = 54;
	v3[59] = 55;
	v3[60] = 56;
	v3[61] = '9';
	v3[62] = '+';
	v3[63] = '/';
	v3[64] = 42;
	v3[65] = 33;
	v3[66] = 64;
	v3[67] = 35;
	v3[68] = 36;
	v3[69] = 37;
	v3[70] = 94;
	v3[71] = 38;
	v3[72] = 40;
	v3[73] = 41;
	v3[74] = 95;
	v3[75] = 63;
	v3[76] = ',';
	v3[77] = '<';
	v3[78] = '>';
	v3[79] = ';';
	v3[80] = '[';
	v3[81] = ']';
	v3[82] = '{';
	v3[83] = '}';
	v3[84] = '~';
	v10 = in;

	
	v9 = len / 3; //ABCD v9 =1 3x8 = 4x6 
	v8 = len > 3 * (len / 3);
	v7 = len == 3 * (len / 3) + 2;
	
	v5 = (char *)malloc(100);
	memset(v5,0,100);

	for (i = 0; i < v9; ++i)
	{
		//‭010000 01  ‭    0100 0010‬‬         ‭01 000011 => ABC
		//000‭10000  0001‭0100    000010‬‬01    00000011
		//v3[16]='Q' v3[20]='U' v3[9]=J   v3[3]=D

		//('A') >>2 = 0001 0000= 16
		*(i + v5) = v3[(*(3 * i + v10) >> 2)];

		//('A') *16 = ‭0100 0001 0000‬ & (0x30)‭0000 0011 0000) = ‭0001 0000‬(16)
		//'B' >> 4  =‭0000 0100‬ && (0x3f)‭0011 1111‬ = 4 | 16 =20
		*(i + 1 + v5) = v3[(char)(16 * *(3 * i + v10) & 0x30) | (char)*(char *)(3 * i + 1 + v10) >> 4 & 0x3F];

		//'B' *4 = ‭0001 0000 1000‬ ‭& 0x3c(‭0000 0011 1100‬) = 0000 ‭0000 1000‬(8)
		//'C' >>6 = ‭0001‬ | 8 = 10‬‬01(9)
		*(i + 2 + v5) = v3[(char)(4 * *(3 * i + 1 + v10) & 0x3C) | (char)*(char *)(3 * i + 2 + v10) >> 6 & 0x3F];
		//'C' >> 0x3F(‭00111111‬) = 00000011(3)
		*(i + 3 + v5) = v3[*(3 * i + 2 + v10) & 0x3F];
		

	}


	if (v8) //v8 = len > 3 * (len / 3);
	{
		//i=1
		//01000100 >> 2 =0010001 =17 =v3[17] = 'R'
		*(4*i + v5) = v3[(char)(*(3 * i + v10) >> 2)];



		if (v7)// v7 = len == 3 * (len / 3) + 2;
		{
			//ABCDE => QUJDREU=
			//0 | ‭0100 0101‬('E') >> 4 = 0000 0100 & ‭00111111‬(0x3F) = 0000 0100(4)
			*(4*i + 1 + v5) = v3[(16 * *(3 * i + v10) & 0x30 | (char)*(char*)(3 * i + 1 + v10)) >> 4 & 0x3F];//v3[4]=E
			//'E'*4 = 0001 0001 0100 & ‭0000 0011 1100‬(0x3c) = 0001 0100(20)
			*(4*i + 2 + v5) = v3[4 * *(3 * i + 1 + v10) & 0x3C];//v3[20] = 'U'
		}

		else
		{

			//ABCD => QUJDRA==
			//'D'*16 = > 0100 0100 0000 & ‭0000 0011 0000‬ = 0
			*(4*i + 1 + v5) = v3[16 * *(3 * i + v10) & 0x30];//v3[0]='A'
			*(4*i + 2 + v5) = 61; // =
		}

		*(4*i + 3 + v5) = 61;// =

	}

	return v5;

}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
