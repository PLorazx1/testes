#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <math.h>

void bi(int n, char arr[], int ult_index){
    int rest;
    if (n%2==0) rest = 48;
    else rest = 49;
    if(n<2) {
        arr[ult_index] = rest;
        if(ult_index >= 0){
            for(int i = ult_index - 1; i>=0; i--){
                arr[i] = 48;
            }
        }
        return;
    }
    else{
        arr[ult_index] = rest;
        return bi(n/2, arr, ult_index - 1);
    }
}

int main(){
    int x;
    char out[9];
    out[8] = '\0';
    printf("Digite o numero para transformar em numeros binarios: ");
    scanf("%d", &x);
    bi(x, out, 7);
    printf("O valor %d em numeros binarios eh simbolizado por %s\n", x, out);
    system("pause");
}