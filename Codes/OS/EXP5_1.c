#include<stdio.h>

int hitCounter=0,faultCounter=0;
void display(int q[], int pf, int hit)
{
    int i;
    if(hit==1)
        printf("\nPage hit");
    else
    {
        faultCounter++;
        printf("\nPage fault");
    }

    for(i=0;i<pf;i++)
    {
        printf(" %d", q[i]);
    }
    printf("\n");
}

void fifopaging(int page[], int n, int pf)
{
    int q[pf], front = 0, i, j, hit = 0;
    for(i = 0; i < pf; i++)
        q[i] = -1;

    for(i = 0; i < n; i++)
    {
        hit = 0;
        for(j = 0; j < pf; j++)
        {
            if(q[j] == page[i]) 
            {
                hit = 1;
                hitCounter++;
                display(q, pf, hit);
                break;
            }
        }
        
        if(hit == 0)
        {
            q[front] = page[i];
            front = (front + 1) % pf; 
            display(q, pf, hit);
        }
    }
}

int main()
{
    int n, page[100], pf;
    printf("Enter no. of pages: ");
    scanf("%d", &n);
    printf("Enter the page reference string: \n");
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &page[i]);
    }
    printf("Enter no. of page frames: ");
    scanf("%d", &pf);
    fifopaging(page, n, pf);
    printf("\nTotal Page Faults: %d\nTotal Page Hits: %d\nHit Ratio: %f", faultCounter, hitCounter, ((hitCounter+0.0)/n));
    return 0;
}
