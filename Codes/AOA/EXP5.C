#include <stdio.h>
#include <string.h>

void print_lcs(char b[10][10], char c[10][10], int i, int j, char X[10]) {
	if (i == 0 || j == 0)
		return;
	if (b[i][j] == 'D') {
		print_lcs(b, c, i - 1, j - 1, X);
		printf("%c", X[i - 1]);
	} else if (b[i][j] == 'U') {
		print_lcs(b, c, i - 1, j, X);
	} else {
		print_lcs(b, c, i, j - 1, X);
	}
}

void lcs(char X[10], char Y[10]) {
	int m, n, i, j;
	char b[10][10];
	int c[10][10];
	
	m = strlen(X);
	n = strlen(Y);
	
	
	for (i = 0; i <= m; i++)
		c[i][0] = 0;
	for (j = 0; j <= n; j++)
		c[0][j] = 0;
		
		
	for (i = 1; i <= m; i++) {
		for (j = 1; j <= n; j++) {
			if (X[i - 1] == Y[j - 1]) {
				c[i][j] = c[i - 1][j - 1] + 1;
				b[i][j] = 'D';
			} else if (c[i - 1][j] >= c[i][j - 1]) {
				c[i][j] = c[i - 1][j];
				b[i][j] = 'U';
			} else {
				c[i][j] = c[i][j - 1];
				b[i][j] = 'L';
			}
		}
	}
	
	
	printf("The Longest Common Subsequence is: ");
	print_lcs(b, (char (*)[10])c, m, n, X);
	printf("\n");
}

int main() {
	char X[10], Y[10];
	
	printf("Enter the First String: ");
	scanf("%s",X);
	printf("Enter the Second String: ");
	scanf("%s",Y);
	
	lcs(X,Y);
	
	return 0;
}
