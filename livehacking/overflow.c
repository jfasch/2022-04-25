#include <stdio.h>


int main(void)
{
    unsigned long number = 18446744073709551615UL;

    printf("size of number: %ld\n", sizeof(number));
    printf("number: %lu\n", number);

    number += 1;

    printf("number: %lu\n", number);
    
    return 0;
}
