#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//Complete the following function.

int marks_summation(int *marks, int number_of_students, char gender)
{
    //Write your code here.
    int result = 0; // Set initial value as 0 to prevent garbage value being allocated to int result
    if (gender == 'b')
    { // Check gender
        for (int i = 0; i <= number_of_students; i += 2)
        { // If gender is b then start from 0 and incrementing by 2 gives 0,2,4,6 i.e. all even places in the marks array and we add it to the result int and return it from function.
            result += marks[i];
        }
    }
    else
    { // No need to check as the other one would be g only
        for (int i = 1; i <= number_of_students; i += 2)
        {
            result += marks[i]; // Here we start from 1 and go to 1,3,5,7 and so on, on incrementing and adding the same indices from array marks to the result int and return that from the function.
        }
    }
    return result;
}

int main()
{
    int number_of_students;
    char gender;
    int sum;

    scanf("%d", &number_of_students);
    int *marks = (int *)malloc(number_of_students * sizeof(int));

    for (int student = 0; student < number_of_students; student++)
    {
        scanf("%d", (marks + student));
    }

    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);

    return 0;
}