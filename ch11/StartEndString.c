#include <stdio.h>

int main(void)
{
	char str[50] = "I like C  programming";
	printf("string: %s \n", str);

	str[8] = '\0';		// 9��° �� �� ���� ����
	printf("string: %s \n", str);

	str[6] = '\0';		// 7��° �� �� ���� ����
	printf("string: %s \n", str);

	str[1] = '\0';		// 2��° �� �� ���� ����
	printf("string: %s \n", str);
	return 0;
}