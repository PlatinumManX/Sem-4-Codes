#include<stdio.h>
#include<conio.h>
void main()
{
	int choice,count=1;
	clrscr();
	printf("1.Increment\n2.Decrement\n3.Disable\n4.Exit");
	do
	{
		printf("\nEnter Your Choice: ");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
				count++;
				asm mov cx, count;
				asm mov ah,01h;
				asm INT 10h;
				break;
			case 2:
				count--;
				asm mov cx, count;
				asm mov ah, 01h;
				asm INT 10h;
				break;
			case 3:
				asm mov cl,20h;
				asm mov ah,01h;
				asm INT 10h;
				break;
		}
	}
	while(choice!=4);
	getch();
}