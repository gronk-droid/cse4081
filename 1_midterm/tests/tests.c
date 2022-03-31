#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int number_three (int m);
int number_four (int n);

// \t of sep:       ────────
// vertical sep:    │
// cross sep:       ┼
// bottom sep:      ┴


int main(int argc, char **argv) {
    /* number 3 */

    printf("\t\t\t\t\t\tsum:\t%d\n", number_three(8));
    printf("\n");
    printf("\n");
    printf("\t\t\t\t\t\tsum:\t%d\n", number_three(12));



    /* number 4 */
    printf("\t\t\t\t\t\tsum:\t%d", number_four(2));
    printf("\n");
    printf("\n");
    printf("\t\t\t\t\t\tsum:\t%d", number_four(3));
    printf("\n");
    printf("\n");
    printf("\t\t\t\t\t\tsum:\t%d", number_four(4));
}

int number_three (int m) {
    int sum = 0;
    int prev_sum = 0;
    printf("m = %d\n\n", m);
    printf("i\t│\tprev_sum\t+\t2^i\t=\tsum\n");
    printf("────────┼────────────────────────────────────────────────────\n");
    for (int i = 1; i < m; i++) {
        prev_sum = sum;
        sum = sum + pow(2, i);
        printf("%d\t│\t%d\t\t+\t2^%d\t=\t%d\n", i, prev_sum, i, sum);
    }
    printf("────────┴────────────────────────────────────────────────────\n");
    return (int) sum;
}

int number_four (int n) {
    int sum = 0;
    int prev_sum = 0;
    int step = 1;
    printf("n = %d\n\n", n);
    printf("step\t│i\t│j\t│sum\t+\t(i * j)\t=\tsum\n");
    printf("────────┼───────┼───────┼────────────────────────────────────────\n");
    for (int i = 0; i < n; i++) {
        for (int j = n; j > 0; j--) {
            prev_sum = sum;
            sum = prev_sum + i * j;
            printf("%d\t│%d\t│%d\t│%d\t+\t(%d * %d)\t=\t%d\n", step, i, j, prev_sum, i, j, sum);
            step++;
        }
    }
    printf("────────┴───────┴───────┴────────────────────────────────────────\n");
    return sum;
}
