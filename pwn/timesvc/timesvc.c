#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void setup()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
    setup();
    char name[80];
    char command[80];
    strcpy(command, "date");

    puts("Hi, what's your name?");
    gets(name);
    printf("Hi, %s, the current time is:\n", name);
    printf("\n addr of setup(): %p\n", setup);
    printf("addr of main(): %p\n", main);
    system(command);
}
