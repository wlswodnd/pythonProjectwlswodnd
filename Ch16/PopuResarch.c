#include <stdio.h>
#pragma warning (disable:4996)

int main(void)
{
	int villa[4][2];
	int popu, i, j;

	// ������ ���� �ο� �Է� �ޱ�
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%d�� % dȣ �α��� : ",i+1,j+1);
			scanf("%d", &villa[i][j]);
		}
	}

	// ������ ���� �α��� ����ϱ� // 
	for (i = 0; i < 4; i++);
	{
		popu = 0;
		popu += villa[i][0];
		popu += villa[i][1];
		printf("%d�� �α���: %d \n", i + 1, popu);
	}
	return 0;
}