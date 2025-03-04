#include<stdio.h>
int main()
{
	int n,j,temp,pro[10],burst[10],prior[10],i,wait[10],turn[10];
	int totalwait=0,totalturn=0;
	printf("Enter Number of processes: ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
		pro[i]=i+1;
	printf("Enter Burst Time of %d Elements:-\n",n);
	for(i=0;i<n;i++)
		scanf("%d",&burst[i]);
	printf("Enter Priority of %d Elements:-\n",n);
	for(i=0;i<n;i++)
		scanf("%d",&prior[i]);
	for(i=0;i<n-1;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(prior[i]==prior[j])
			{
				if(burst[i]>burst[j])
				{
					temp=prior[i];
					prior[i]=prior[j];
					prior[j]=temp;
					temp=pro[i];
					pro[i]=pro[j];
					pro[j]=temp;
					temp=burst[i];
					burst[i]=burst[j];
					burst[j]=temp;
				}
			}
			else if(prior[i]>prior[j])
			{
				temp=prior[i];
				prior[i]=prior[j];
				prior[j]=temp;
				temp=pro[i];
				pro[i]=pro[j];
				pro[j]=temp;
				temp=burst[i];
				burst[i]=burst[j];
				burst[j]=temp;
			}
		}
	}
	wait[0]=0;
	for(i=1;i<n;i++)
		wait[i]=wait[i-1]+burst[i-1];
	for(i=0;i<n;i++)
	{
		turn[i]=wait[i]+burst[i];
		totalwait=totalwait+wait[i];
		totalturn=totalturn+turn[i];
	}
	printf("\nProcess\tBurst Time\tPriority\tWaiting Time\tTurnaround Time\n");
	for(i=0;i<n;i++)
		printf("P%d\t%d\t\t%d\t\t%d\t\t%d\n",pro[i],burst[i],prior[i],wait[i],turn[i]);
	printf("\nAverage Waiting Time: %.2f time units\n",(float)totalwait/n);
	printf("Average Turnaround Time: %.2f time units",(float)totalturn/n);
	return 0;
}
