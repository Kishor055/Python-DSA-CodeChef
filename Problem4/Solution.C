#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* remove_outer_parentheses(char* s) {
    int len = strlen(s);
    // Allocate memory for the result (same size as input + null terminator)
    char* result = (char*)malloc((len + 1) * sizeof(char));
    int depth = 0;
    int j = 0; // Index for the result string

    for (int i = 0; i < len; i++) {
        char ch = s[i];
        if (ch == '(') {
            if (depth > 0) {
                result[j++] = ch;
            }
            depth++;
        } else {
            depth--;
            if (depth > 0) {
                result[j++] = ch;
            }
        }
    }

    result[j] = '\0'; // Properly terminate the string
    return result;
}

int main() {
    char s[] = "(()())(())";
    char* clean_string = remove_outer_parentheses(s);
    
    printf("%s\n", clean_string); // Output: ()()()

    free(clean_string); // Always free malloc'd memory
    return 0;
}
