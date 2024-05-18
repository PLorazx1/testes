#include <stdio.h>


int main(){  
    int i, n, maior, quant;
    maior = 0;
    quant = 0;
    printf("Quantos numeros voce vai digitar?\n");
    scanf("%d", &i);
    for(;i>0;i--){
        printf("Digite qualque valor: ");
        scanf("%d", &n);
        if(n>maior){
            maior = n;
            quant = 1;
            continue;
        }if(n==maior){
            quant += 1;
        }
    }
    printf("o maior numero, %d, foi digitado %d vezes\n", maior, quant);
    system("pause");
    return 0;
}
