#include <stdio.h>

int main() {
    int T;
    // Read the number of test cases
    if (scanf("%d", &T) != 1) return 0;

    while (T--) {
        int N;
        // Read the size of the array
        if (scanf("%d", &N) != 1) continue;

        int max_height;
        int current_height;

        // Process the first element to initialize max_height
        scanf("%d", &max_height);

        // Process the remaining N-1 elements
        for (int i = 1; i < N; i++) {
            scanf("%d", &current_height);
            if (current_height > max_height) {
                max_height = current_height;
            }
        }

        // Print the result for the current test case
        printf("%d\n", max_height);
    }

    return 0;
}
