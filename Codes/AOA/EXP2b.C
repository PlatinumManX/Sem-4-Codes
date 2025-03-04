#include<stdio.h>
int pass=1;
void quicksort(int A[], int low, int high, int n)
{
	int pivot,i,j,temp,pi;
	if(low<high)
	{
		pivot=A[high];
		i=low-1;
		for(j=low;j<high;j++)
		{
			if(A[j]<pivot)
			{
				i++;
				temp=A[i];
				A[i]=A[j];
				A[j]=temp;
			}
		}
		temp=A[i+1];
		A[i+1]=A[high];
		A[high]=temp;
		pi=i+1;
		printf("Pass %d: ",pass);
		for(i=0;i<n;i++)
			printf("%d\t",A[i]);
		printf("\n");
		pass++;
		quicksort(A,low,pi-1,n);
		quicksort(A,pi+1,high,n);
	}
}
int main()
{
	int i,A[10],n;
	printf("Enter the Number of Elements: ");
	scanf("%d",&n);
	printf("Enter the Elements:-\n");
	for(i=0;i<n;i++)
		scanf("%d",&A[i]);
	printf("Sorting using Quick Sort:-\n");
	quicksort(A,0,n-1,n);
	printf("Sorted Array is:- ");
	for(i=0;i<n;i++)
		printf("%d\t",A[i]);
	return 0;
}
