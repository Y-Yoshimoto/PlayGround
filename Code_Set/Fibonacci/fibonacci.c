#include <stdio.h>

int fib(n){
    return (n > 1)? fib(n-2)+fib(n-1):((n == 1)? 1:0);
}

int main(int argc,char * argv[]){
    int max = 9;
    for(int i = 0; i < max; i++){
        printf("%d,",fib(i));
    }
    printf("%d\n",fib(max));
    return 0;
}
