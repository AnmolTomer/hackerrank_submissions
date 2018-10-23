#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>

void main(){
    int a,i,d;
    scanf("%d",&a);
	for(i=1;i<11;i++)
    {
        d = i*a;    
        printf("%d x %d = %d\n",a,i,d);    
    }
}

