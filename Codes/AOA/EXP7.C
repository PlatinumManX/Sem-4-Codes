#include <stdio.h>
#include <limits.h>
#define INF 99999
#define N 3
void printSolution(int dist[N][N], int pred[N][N])
{
    printf("Shortest Distance Matrix:\n");
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (dist[i][j] == INF)
            {
                printf("%s", "INF");
                printf("\n\t");
            }
            else
                printf("%d\t", dist[i][j]);
        }
        printf("\n");
    }
    printf("\nPredecessor Matrix:\n");
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (pred[i][j] == -1)
            {
                printf("%s", "NIL");
                printf("\t");
            }
            else
                printf("%d\t", pred[i][j] + 1);
        }
        printf("\n");
    }
}
void floydWarshall(int graph[N][N])
{
    int dist[N][N], pred[N][N];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            dist[i][j] = graph[i][j];
            if (graph[i][j] != INF && i != j)
                pred[i][j] = i;
            else
                pred[i][j] = -1;
        }
    }
    for (int k = 0; k < N; k++)
    {
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    pred[i][j] = pred[k][j];
                }
            }
        }
    }
    printSolution(dist, pred);
}
int main() {
    int graph[N][N];
    printf("Enter the Adjacency Matrix:-\n");
    for(int i=0;i<N;i++)
    {
		for(int j=0;j<N;j++)
			scanf("%d",&graph[i][j]);
	}
    floydWarshall(graph);
    return 0;
}

