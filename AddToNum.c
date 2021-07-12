#include <stdio.h>
#pragma warning (disable:4996)

int main(void)
{
	int total = 0;
	int i, num;
	printf("0ºÎÅÍ num±îÁöÀÇ µ¡¼À, numÀº? ");
	scanf("%d", &num);

	for (i = 0; i < num + 1; i++)
		total += 1;


	printf("0ºÎÅÍ %d±îÁö µ¡¼À°á°ú: %d \n", num, total);
	return 0;
}