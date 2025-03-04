#include<stdio.h>
int main()
{
	int j,key,i,a[100],n,k;
	printf("Enter the Number of Elements: ");
	scanf("%d",&n);
	printf("Enter the Elements:-\n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("List before Sorting is:- ");
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);
	printf("\n");
	for(j=1;j<n;j++)
	{
		key=a[j];
		i=j-1;
		while(i>=0 && a[i]>key)
		{
			a[i+1]=a[i];
			i=i-1;
		}
		a[i+1]=key;
		printf("List after Iteration %d is:- ",j);
		for(k=0;k<n;k++)
			printf("%d\t",a[k]);
		printf("\n");
	}
	printf("\nThe Sorted List after Insertion Sort is:- ");
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);
}	
	
