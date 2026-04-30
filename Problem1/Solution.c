#include <stdio.h>

int main() {
    int N, X;

    // Read N and X
    if (scanf("%d %d", &N, &X) != 2) return 0;

    int A[N];
    int found = 0;

    // Read array A and check for X simultaneously
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
        if (A[i] == X) {
            found = 1;
        }
    }

    // Check if X was found
    if (found) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
