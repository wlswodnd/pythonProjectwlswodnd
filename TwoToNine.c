#include <stdio.h>

int main(void)
{
	int cur = 2;
	int is = 0;
	while (cur < 10)	// 2�ܺ��� 9�ܱ��� �ݺ�
	{
		printf("----%d��----\n", cur);
		is = 1;			// ���ο� ���� ������ ���ؼ�
		while (is < 10)	// �� ���� 1���� 9�� ���� ǥ��
		{
			printf(" %d x %d = %d\n", cur, is, cur * is);
			is++;
		}
		cur++;			// ���� ������ �Ѿ��
		printf("\n");
	}
	return 0;
}