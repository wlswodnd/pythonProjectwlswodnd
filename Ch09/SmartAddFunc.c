#include <stdio.h>
//#pragma warning(disable:4996)

int Add(int num1, int num2)		// �������� (o), ��ȯ �� (o)
{
	return num1 + num2;
}

void ShowAddResult(int num)		// �������� (o), ��ȯ �� (x)
{
	printf("���� ��� ���: %d \n", num);
}
int ReadNum(void)		// �������� (x), ��ȯ �� (o)
{
	int num;
	scanf("%d", &num);
	return num;
}

void HowToUseThisProg(void)		// �������� (x), ��ȯ �� (x)
{
	printf("�� ���� ������ �Է��Ͻø� ��������� ��µ˴ϴ�. \n");
	printf("��! �׷� �� ���� ������ �Է��ϼ���. \n");
}

int main(void)
{
	int result, num1, num2;
	HowToUseThisProg();
	num1 = ReadNum();
	num2 = ReadNum();
	result = Add(num1, num2);
	ShowAddResult(result);
	return 0;
}