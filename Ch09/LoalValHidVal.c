#include <stdio.h>

int main(void)
{
	int num = 1;

	if (num == 1)
	{
		int num = 7;		// �� ���� �ּ�ó�� �ϰ� ������ Ȯ������!
		num += 10;
		printf("if�� �� �������� num: %d \n", num);
	}
	printf("main �Լ� �� �������� num: %d \n", num);
	return 0;
}