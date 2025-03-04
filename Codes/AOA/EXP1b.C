#include<stdio.h>
int main()
{
	int index,j,k,temp,i,a[100],n;
	printf("Enter the Number of Elements: ");
	scanf("%d",&n);
	printf("Enter the Elements:-\n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("List before Sorting is:- ");
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);
	printf("\n");
	for(i=0;i<n;i++)
	{
		index=i;
		for(j=i+1;j<n;j++)
		{
			if(a[j]<a[index])
				index=j;
		}
		temp=a[i];
		a[i]=a[index];
		a[index]=temp;
		printf("List after Iteration %d is:- ",i);
		for(k=0;k<n;k++)
			printf("%d\t",a[k]);
		printf("\n");
	}
	printf("\nThe Sorted List is after Selection Sort is:- ");
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);
}
