#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int size;
    scanf("%d",&size);
    if(size == 0){
        printf("-1");
        return 0;
    }
    
    int array[size];
    for(int i=0; i<size; i++){
        scanf("%d",&array[i]);
    }
    
    int minimum = array[0];
    int index = 0;
    for(int i=0; i<size; i++){
        if(array[i]<minimum){
            minimum = array[i];
            index = i;
        }
    }
    
    printf("%d",index);
    printf("\n%d",minimum);
    
    return 0;
}
