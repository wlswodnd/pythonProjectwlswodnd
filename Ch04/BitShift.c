#include <stdio.h>

int main(void)
{
	int num = 15;				// 00000000 00000000 00000000 00001111
	int result1 = num << 1;		// num의 비트 열을 왼쪽으로 1칸씩 이동
	int result2 = num << 2;		// num의 비트 열을 왼쪽으로 2칸씩 이동
	int result3 = num >> 1;		// num의 비트 열을 오른쪽으로 1칸씩 이동
	printf("1칸 왼쪽으로 이동 결과: %d \n", result1);
	printf("2칸 왼쪽으로 이동 결과: %d \n", result2);
	printf("1칸 오른쪽으로 이동 결과: %d \n", result3);
	return 0;
}