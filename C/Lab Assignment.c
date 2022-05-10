//Assignment 2
// Write a C program to prompt the user to input 3-digit number and print these values in forward and reversed order
#include<stdio.h>
//#include<conio.h>
void main()
{
    int a, b, c;
    printf("input a 3-digit no. ");
    scanf ("%d", &a);
    printf("The forward order is %d\n", a);
    b = a / 100;
    a = a%100;
    c = a/10;
    a = a%10;
    a = 100*a + 10*c + b;
    printf ("The reversed order is %d\n", a);
    //getch();
}

// Write a program to swap two variables values with and without using third variables
#include <stdio.h>
//#include<conio.h>
void main()
{
    int a, b;
    printf ("Input value for two variables\n");
    scanf("%d%d", &a, &b);
    printf("Initially a is %d and b is %d\n", a, b);
    a = a + b;
    b = a - b;
    a = a -b;
    printf("After swapping a is %d and b is %d \n", a, b);
    //getch();
}

// Write a program to check odd or even number (a) using modulus operator
#include<stdio.h>
//#include<conio.h>
int main()
{
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);
    if (num % 2 == 0)
        printf("%d is even.", num);
    else
        printf("%d is odd.", num);
    return 0;
}
//(b) using conditional operator
#include <stdio.h>
//#include<conio.h>
int main()
{
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);
    (num % 2 == 0) ? printf("%d is even.", num) : printf("%d is odd.", num);
    return 0;
}

// Write a program to print the size of char, float, double and long double data types in C.
#include <stdio.h>
int main()
{
    int intType;
    float floatType;
    double doubleType;
    char charType;

    // sizeof evaluates the size of a variable
    printf("Size of int: %zu bytes\n", sizeof(intType));
    printf("Size of float: %zu bytes\n", sizeof(floatType));
    printf("Size of double: %zu bytes\n", sizeof(doubleType));
    printf("Size of char: %zu byte\n", sizeof(charType));

    return 0;
}


