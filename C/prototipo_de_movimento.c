#include <stdio.h>


int main(){  
    int matriz[10][10], X=0, Y=0;
    char input  = 'c';
    for (int y=0; y<10; y++){
        for (int x=0; x<10; x++){
            if(x==X && y==Y){
                matriz[y][x] = 1;
            }
            else{
                matriz[y][x] = 0;
            }
        }
    }
    while (input != '0'){
        for (int y=0; y<10; y++){
        for (int x=0; x<10; x++){
            printf("%3d ", matriz[y][x]);

            }
        printf("\n");
        }
        scanf("%c", &input);
        if(input == 'w' || input == 'W'){
            Y -= 1;
        }if(input == 's' || input == 'S'){
            Y += 1;
        }if(input == 'a' || input == 'A'){
            X -= 1;
        }if(input == 'd' || input == 'D'){
            X += 1;
        }
        for (int y=0; y<10; y++){
            for (int x=0; x<10; x++){
                if(x==X && y==Y){
                    matriz[y][x] = 1;
                }
                else{
                    matriz[y][x] = 0;
                }
        }
        system("cls");
    }
    }
    system("pause");
    return 0;
}
