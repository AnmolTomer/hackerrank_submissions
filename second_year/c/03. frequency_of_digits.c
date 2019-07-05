#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char str[1001]; //Declare character array
    scanf("%s", str);
    int freq[10] = {0};
    for (int i = 0; i < strlen(str); ++i)
    {
        if (str[i] >= '0' && str[i] <= '9')
        {
            ++freq[str[i] - '0']; // '0' = 48 Subtracting it from any number to remove ASCII value and get int value
        }
    }
    for (int i = 0; i < 10; ++i) // for printing
    {
        printf("%d ", freq[i]);
    }
    return 0;
}

/*
https://www.hackerrank.com/challenges/frequency-of-digits-1

lw4n88j12n1
0 2 1 0 1 0 0 0 2 0 

1v88886l256338ar0ekk
1 1 1 2 0 1 2 0 5 0
 */