#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

void calculate_the_maximum(int n, int k)
{
    //Write your code here.
    int and_max = 0; // Initialize with 0
    int or_max = 0;
    int xor_max = 0;
    for (int i = 1; i <= n; i++) // Multiple loops to compare n and n+1th number
    {
        for (int j = i + 1; j <= n; j++)
        {
            if (((i & j) > and_max) && ((i & j) < k))
            {
                and_max = i & j;
            }
            if (((i | j) > or_max) && ((i | j) < k))
            {
                or_max = i | j;
            }
            if (((i ^ j) > xor_max) && ((i ^ j) < k))
            {
                xor_max = i ^ j;
            }
        }
    }
    printf("%d\n%d\n%d\n", and_max, or_max, xor_max);
}

int main()
{
    int n, k;

    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    return 0;
}
// Problem https://www.hackerrank.com/challenges/bitwise-operators-in-c/problem