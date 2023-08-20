#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int array_size_1;
    scanf("%d",&array_size_1);
    
    int array_1[array_size_1];

    for(int i = 0; i<array_size_1; i++)
    {
        scanf("%d ",&array_1[i]);
    }
    
    int array_size_2;
    scanf("%d",&array_size_2);
    
    int array_size = array_size_1 + array_size_2;
    
    if(array_size == 0)
    {
        printf("-1");
        return 0;
    }
    
    int array[array_size];

    int j;
    for(j=0; j<array_size_2; j++)
    {
        scanf("%d ",&array[j]);
    }
    
    for(int k = 0; k<array_size_1; k++)
    {
        array[j] = array_1[k];
        j++;
    }
    
    for(int j=0; j<array_size; j++)
    {
        for(int i = 1; i<array_size-j; i++)
        {
            if(array[i]<array[i-1])
            {
                int temporary = array[i-1];
                array[i-1] = array[i];
                array[i] = temporary;
            }
        }
    }
    
    for(int i = 0; i<array_size; i++)
    {
        printf("%d ",array[i]);
    }
    return 0;
}