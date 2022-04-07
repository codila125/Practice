#include<stdio.h>
int main()
{
    printf("Hello World");
    printf("teri meri walli");
}

#include <stdio.h>
int main()
{ int a = 1, b = 2, sum;
float s = 2.03;
sum = a + b;
printf("%d\t%d\n", a, b);
printf("the sum is %d\n", sum);
printf("the given float is %f\n", s);
}

#include<stdio.h>
int main()
{
    int a, b, c;
    printf("Enter Three Numbers ");
    scanf("%d%d%d", &a,&b,&c);
    printf("the three numbers are \t %d\t%d\t%d\n", a,b,c);
    if (a > b && a > c)
        printf("%d is the greatest among three numbers", a);
    else if (b > a && b > c)
        printf("%d is the greatest among three numbers", b);
    else
        printf("%d is the greatest among three numbers", c);
}