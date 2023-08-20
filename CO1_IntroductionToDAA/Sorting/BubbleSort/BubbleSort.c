#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

int main()
{
    int array_size;
    scanf("%d",&array_size);
    
    int array[array_size];

    for(int i = 0; i<array_size; i++)
    {
        scanf("%d ",&array[i]);
    }
    
    if(array_size == 0)
    {
        printf("-1\n\n-1\n\n-1");
        return 0;
    }
    
    int comparisons = 0, swaps = 0;
    
    for(int j=0; j<array_size; j++)
    {
        for(int i = 1; i<array_size-j; i++)
        {
            if(array[i]<array[i-1])
            {
                int temporary = array[i-1];
                array[i-1] = array[i];
                array[i] = temporary;
                swaps++;
            }
            comparisons++;
        }
    }

    printf("%d\n\n",comparisons);
    printf("%d\n\n",swaps);
    for(int i = 0; i<array_size; i++)
    {
        printf("%d ",array[i]);
    }
    return 0;
}