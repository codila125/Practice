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
printf("%d\t%d\n", a, b);    //%d is for integers and %f is for float
printf("the sum is %d\n", sum);    //\t provides space equal to a tab adn \n provides space equal to a line
printf("the given float is %f\n", s);
}

#include<stdio.h>
void main()
{
    int a, b, c;
    printf("Enter Three Numbers ");
    scanf("%d%d%d", &a,&b,&c);  //&a in this line is used during user inputs
    printf("the three numbers are \t %d\t%d\t%d\n", a,b,c);
    if (a > b && a > c)                                     //&& means "and", || means "or", ! means "not"
        printf("%d is the greatest among three numbers", a);
    else if (b > a && b > c)
        printf("%d is the greatest among three numbers", b);
    else
        printf("%d is the greatest among three numbers", c);
}