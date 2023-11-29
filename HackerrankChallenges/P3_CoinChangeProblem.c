#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int minimumCoins(int total, int denominations[], int numDenominations) {
    if (total == 0) {
        return 0;
    }

    int minCoins = -1;  // Not possible

    for (int i = 0; i < numDenominations; i++) {
        if (total - denominations[i] >= 0) {
            int subProblem = minimumCoins(total - denominations[i], denominations, numDenominations);
            if (subProblem != -1) {
                if (minCoins == -1 || subProblem + 1 < minCoins) {
                    minCoins = subProblem + 1;
                }
            }
        }
    }
    return minCoins;
}

int main() {
    int numDenominations;
    scanf("%d", &numDenominations);

    int denominations[numDenominations];
    for (int i = 0; i < numDenominations; i++) {
        scanf("%d", &denominations[i]);
    }

    int total;
    scanf("%d", &total);

    printf("%d\n", minimumCoins(total, denominations, numDenominations));

    return 0;
}