#include <stdio.h>

const char* check_coupon(int n, int x, int y, int prices[]) {
    int save = 0;

    for (int i = 0; i < n; i++) {
        if (prices[i] >= y) {
            save += y;
        } else {
            save += prices[i];
        }
    }

    if (save > x) {
        return "COUPON";
    } else {
        return "NO COUPON";
    }
}

int main() {
    // Example usage:
    int prices[] = {50, 100, 20};
    int n = 3;
    int x = 100;
    int y = 40;

    printf("%s\n", check_coupon(n, x, y, prices));

    return 0;
}
