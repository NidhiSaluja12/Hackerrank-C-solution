#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
  
  char C;
  char lang[50];
  char greet[100];
  scanf("%c", &C);
  scanf("%s", &lang);
  scanf("\n");
  scanf("%[^\n]%*c", &greet);
  printf("%c\n%s\n%s", C, lang, greet);
  
  return 0;
}
