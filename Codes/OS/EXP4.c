#include <stdio.h>
#include <stdlib.h>

// node == memory block
struct node
{
    int size;
    int status;
    int process;
    struct node *link;
};
struct node *newnode = NULL;
struct node *start = NULL;
struct node *temp = NULL;
struct node *temp2 = NULL;
struct node *ptr = NULL;

// functions
void create_nodes();
void display();
void first_fit();
void best_fit();
void worst_fit();

// declarations

void main()
{
    int sv = 0, flagg = 1;
    do
    {
        printf("\n\n Menu:\n");
        printf(" 1. Enter new memory block\n");
        printf(" 2. First Fit\n");
        printf(" 3. Best Fit\n");
        printf(" 4. Worst Fit\n");
        printf(" 5. Display\n");
        printf(" 6. exit\n");
        printf(" Enter your option: ");
        scanf("%d", &sv);

        switch (sv)
        {
        case 1:
            create_nodes();
            display();
            break;

        case 2:
            first_fit();
            break;

        case 3:
            best_fit();
            break;

        case 4:
            worst_fit();
            break;

        case 5:
            display();
            break;

        case 6:
            flagg = 0;
            break;
        }
    } while (flagg == 1);
}

void display()
{
    int sr = 1;
    ptr = start;
    printf("--------------\nLinked List");
    printf(" \nSrNo.\t Memory    Status   Prcoess \t\t This \t\t Next\n");

    while (ptr != NULL || ptr != 0)
    {
        printf("%d",sr);
        printf("\t");
        printf(" %d", ptr->size);
        printf("\t");
        if(ptr->status == 1)
            printf(" Free \t\t");
        else
            printf(" Not Free\t");
        printf(" %d", ptr->process);
        printf("\t\t");
        printf(" %d", ptr);
        printf("\t\t");
        printf(" %d", ptr->link);
        printf("\n");
        ptr = ptr->link;
        sr += 1;
    }
    printf("\n--------------\n");
}

void create_nodes()
{
    int i, n;
    printf("\n Enter the no. of memory blocks: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        temp = newnode;
        newnode = (struct node *)malloc(sizeof(struct node));

        printf("\n Enter memory size: ");
        scanf("%d", &newnode->size);

        printf(" Enter its status [1 for free, 0 for not free]: ");
        scanf("%d", &newnode->status);

        if(newnode->status == 0)
        {
        printf(" Enter the process it has: ");
        scanf("%d", &newnode->process);
        }
        else
            newnode->process = 0;

        newnode->link = NULL;

        if (start == NULL)
        {

            start = newnode;
        }

        else
        {
            temp = start;
            while (temp->link != NULL)
            {
                temp = temp->link;
            }
            temp->link = newnode;
        }
    }
}

void first_fit()
{
    int f = 0;
    int name,siz;
    temp = start;

    printf("\n Enter the process name: ");
    scanf("%d", &name);

    printf("\n Enter the process size: ");
    scanf("%d", &siz);

    printf("\n Entered process: %d and its size: %d",name,siz);

    while( temp != NULL || temp != 0)
    {
        if( temp->status == 1 && temp->size >= siz)
            {
                temp->status = 0;
                temp->process = name;
                f = 1;
                break;
            }
        else
            temp = temp->link;
    }
        if(f == 0)
            printf("\n No Vacant Location || Failed");
		
        printf("\n First Fit Memory: %d", temp->size);



}

void best_fit()
{
    int min = 10000,name,siz;
    temp = start;
    temp2 = start;

    printf("\n Enter the process name: ");
    scanf("%d", &name);

    printf("\n Enter the process size: ");
    scanf("%d", &siz);

    printf("\n Entered process: %d and its size: %d",name,siz);

    while (temp != NULL)
    {
        if(temp->status == 1 && temp->size >= siz && temp->size < min)
        {
            min = temp->size;
            temp2 = temp;
            temp = temp->link;
        }
        else
            temp = temp->link;
    }

    if(min == 10000)
        printf("\n Failed No space available: ");

    else
    {
        printf("\n Best Fit Memory: %d", min);

        temp2->process = name;
        temp2->status = 0;
    }
}

void worst_fit()
{
    int max = 0, name = 0, siz = 0;
    temp = start;
    temp2 = start;

    printf("\n Enter the process name: ");
    scanf("%d", &name);

    printf("\n Enter the process size: ");
    scanf("%d", &siz);

    printf("\n Entered process: %d and its size: %d",name,siz);

    while (temp != NULL)
    {
        if(temp->status == 1 && temp->size >= siz && temp->size > max)
        {
            max = temp->size;
            temp2 = temp;
        }
        temp = temp->link;
    }

    if(max == 0)
        printf("\n Failed No space available: ");

    else
    {
        printf("\n Worst Fit Memory: %d", max);

        temp2->process = name;
        temp2->status = 0;
    }
}



