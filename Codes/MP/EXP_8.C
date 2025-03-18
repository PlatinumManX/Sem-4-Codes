#include<stdio.h>
#include<conio.h>
void main()
{
	int a,b,gcd;
	clrscr();
	printf("Ahmed Ansari C-11 09\n");
	printf("Enter Two Numbers: ");
	scanf("%d%d",&a,&b);
	asm mov AX ,a;
	asm mov BX ,b;

	UP1:
	asm SUB BX , AX;
	UP2:
	asm SUB AX , BX;

	asm CMP AX , BX;
	asm JZ DOWN;
	asm JC UP1;
	asm JNC UP2;

	DOWN:
	asm MOV gcd , BX;
	printf("GCD is %d",gcd);
	getch();
}