#include <stdio.h>
#define SIZE 5

int main()
{
    // Input of array elements
    int array[SIZE];
    for(int i=0; i<SIZE; i++)
    {
        scanf("%d ", &array[i]);
    }

    int max = SIZE%2 == 0 ? SIZE/2 : (SIZE-1)/2;

    // Reversing the array
    for(int i=0; i<max; i++)
    {
        int temp = array[i];
        array[i] = array[SIZE-i];
        array[SIZE-i] = temp;
    }

    // Displaying reversed array
    for(int i=0; i<SIZE; i++)
    {
        printf("%d ", array[i]);
    }
    return 0;
}