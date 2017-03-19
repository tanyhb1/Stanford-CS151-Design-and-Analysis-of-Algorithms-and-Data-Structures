#include <stdio.h>

int main()
{
	int x = 3;
	int y = 4;
	printf("the value of x and y are %d and %d respectively.\n", x, y);
	int temp = x;
	x = y;
	y = temp;
	printf("the value of x and y are %d and %d respectively.\n", x, y);
	return 0;
}
