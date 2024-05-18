#include <stdio.h>

int main(){
    int ult, pnult, n, i;
    ult = 1;
    pnult = 0;
    printf("digite qualquer numero: ");
    scanf("%d", &n);
    if(n==0){
        printf("o %d termo eh o numero: %d\n", n, pnult);
    }else{
        for(i=2;i<=n;i++){
            ult += pnult;
            pnult = ult - pnult;
        }
        printf("o %d termo eh o numero: %d\n", n, ult);
    }
    system("pause");
    return 0;
}