#include <stdio.h>
#include <stdlib.h>
#define INF 9999

int V, E = 0;
int G[10][10];

int pi[10], key[10];
int priority[10]; 
int vertex_queue[10]; 

int startvertex;
int rear = -1;

void readGraph() {
    printf("\nEnter adjacency matrix \n");
    E = 0;
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            scanf("%d", &G[i][j]);
            if (G[i][j] != 0 && i < j) {
                E++;  // Avoid double counting edges
            }
        }
    }
}

void displaygraph() {
    printf("\nGraph is... \n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            printf("%d\t", G[i][j]);
        }
        printf("\n");
    }
}

void initialize() {
    for (int i = 0; i < V; i++) {
        key[i] = INF;
        pi[i] = -1;
        vertex_queue[i] = i;
    }
    key[startvertex] = 0;
}

void print1Darray(const char *str, int a[], int s, int e) {
    printf("\n%s [] : ", str);
    for (int i = s; i < e; i++) {
        printf("\t%d", a[i]);
    }
    printf("\n");
}

void createQueue() {
    for (int i = 0; i < V; i++) {
        priority[i] = key[i];
    }
    rear = V - 1;
    printf("\n\nPriority Array after creating queue : \n");
    print1Darray("Queue array", vertex_queue, 0, rear+1);
    print1Darray("Priority array", priority, 0, rear+1);
}

int Extract_Min() {
    int min = INF, min_index = -1;
    
    for (int i = 0; i <= rear; i++) {
        if (priority[i] < min) {
            min = priority[i];
            min_index = i;
        }
    }

    if (min_index == -1) {
        return -1;
    }

    int vertex = vertex_queue[min_index];

    // Remove min element from priority queue
    for (int i = min_index; i < rear; i++) {
        priority[i] = priority[i + 1];
        vertex_queue[i] = vertex_queue[i + 1];
    }
    rear--;
    printf("\nPriorirty Queue after extracting vertex %d\n",vertex);
    print1Darray("Queue array", vertex_queue, 0, rear+1);
    print1Darray("Priority array", priority, 0, rear+1);
    return vertex;
}

void printpath(int s, int v) {
    if (v == s)
        printf(" %d ", s);
    else if (pi[v] == -1)
        printf("No path exists");
    else {
        printpath(s, pi[v]);
        printf(" --> %d ", v);
    }
}

void dijkstra() {
    createQueue();
    
    while (rear >= 0) {
        int u = Extract_Min();
        if (u == -1) break;  // No more reachable nodes
        
        for (int v = 0; v < V; ++v) {
            if (G[u][v] != 0) {
                if (key[u] + G[u][v] < key[v]) {
                    pi[v] = u;
                    key[v] = key[u] + G[u][v];

                    // Decrease-key operation
                    for (int i = 0; i <= rear; i++) {
                        if (vertex_queue[i] == v) {
                            priority[i] = key[v];
                            break;
                        }
                    }
                }
            }
        }
    }
}

int main() {
    printf("\nEnter number of vertices: ");
    scanf("%d", &V);
    
    readGraph();
    displaygraph();
    printf("No. of vertices: %d\nNo. of edges: %d\n", V, E);
    
    printf("\nEnter starting vertex: ");
    scanf("%d", &startvertex);

    initialize();
    
    printf("\nAfter initialization....");
    print1Darray("KEY array", key, 0, V);
    print1Darray("PI array", pi, 0, V); 
    printf("\n");

    dijkstra();
    
    printf("\n\nFinal Values are.........");
    print1Darray("KEY array", key, 0, V);
    print1Darray("PI array", pi, 0, V); 

    printf("\n\n\nPrinting Paths\n");
    for (int i = 0; i < V; i++) {
        if (i == startvertex)
            continue;
        printf("Path from %d to %d is ", startvertex, i);  
        printpath(startvertex, i);
        printf("\n");
    }

    return 0;
}
