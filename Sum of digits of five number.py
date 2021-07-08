#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int n;
    int sum=0;
    int temp,digit;
    
    scanf("%d", &n);
    temp = n;
    while (temp>0)
    {
        digit = temp%10;
        sum+=digit;
        temp = temp/10;
        
        
    }
    printf("%d",sum);
    return 0;
    
    
    
    //Complete the code to calculate the sum of the five digits on n.
    
}

