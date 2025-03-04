#include <stdio.h>

int knapsack(int capacity, int weight[], int value[], int n) {
    int dp[capacity + 1]; 
    for (int i = 0; i <= capacity; i++)
        dp[i] = 0;

    for (int i = 0; i < n; i++) {
        for (int w = capacity; w >= weight[i]; w--) {
            int newValue = value[i] + dp[w - weight[i]];
            if (newValue > dp[w])
                dp[w] = newValue;
        }
    }
    return dp[capacity];
}

int main() {
    int value[10], weight[10], capacity, n;

    printf("Enter the Number of Items: ");
    scanf("%d", &n);

    printf("Enter the Values of Items: ");
    for(int j = 0; j < n; j++)
        scanf("%d", &value[j]);

    printf("Enter the Weights of Items: ");
    for(int j = 0; j < n; j++)
        scanf("%d", &weight[j]);

    printf("Enter the Capacity of the Knapsack: ");
    scanf("%d", &capacity);

    printf("Maximum value in Knapsack = %d\n", knapsack(capacity, weight, value, n));
    return 0;
}

