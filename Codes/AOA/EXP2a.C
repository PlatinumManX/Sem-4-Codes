#include <stdio.h>
int pass=1;
void merge(int A[], int low, int mid, int high, int n)
{
    int l = low;
    int r = mid + 1;
    int i = low;
    int b[100];
    while(l<=mid&&r<=high)
    {
        if (A[l]<=A[r])
        {
            b[i]=A[l];
            l++;
        }
        else
        {
            b[i]=A[r];
            r++;
        }
        i++;
    }
    while(l<=mid)
    {
        b[i]=A[l];
        l++;
        i++;
    }
    while(r<=high)
    {
        b[i]=A[r];
        r++;
        i++;
    }
    for(i=low;i<=high;i++)
        A[i]=b[i];
    printf("Pass %d:-\t",pass);
    for(i=0;i<n;i++)
		printf("%d\t",A[i]);
	printf("\n");
	pass++;
}
void mergesort(int A[], int low, int high, int n)
{
    if(low<high)
    {
        int mid=(low+high)/2;
        mergesort(A,low,mid,n);
        mergesort(A,mid+1,high,n);
        merge(A,low,mid,high,n);
    }
}
int main()
{
    int A[10];
    int i,n;
    printf("Enter the Number of Elements: ");
    scanf("%d",&n);
    printf("Enter the Elements:\n");
    for(i=0;i<n;i++)
        scanf("%d", &A[i]);
    printf("Sorting using Merge Sort is:-\n");
    mergesort(A, 0, n - 1, n);
    printf("Sorted Elements:\n");
    for (i = 0; i < n; i++)
        printf("%d ", A[i]);
    printf("\n");
    return 0;
}
