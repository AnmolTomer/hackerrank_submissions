#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int n;
    scanf("%d", &n);
    int length = 2 * n - 1;
    // Complete the code to print the pattern.
    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
            int min = i < j ? i : j;                           // If i < j : min = i else min = j
            min = min < length - i ? min : length - i - 1;     // For rows
            min = min < length - j - 1 ? min : length - j - 1; // For columns

            printf("%d ", n - min);
        }
        printf("\n");
    }
    return 0;
}
