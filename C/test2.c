#include<stdio.h>
#include<stdlib.h>
#include<windows.h>

int main(){
    float valor1, valor2;
    float soma, sub, mult, div;
    int escolha;
    int i =0;
    while (i == 0){
        printf("=-=-=-=-=-=-=-=-\n");
        printf("   Calculadora  \n");
        printf("-=-=-=-=-=-=-=-=\n");
        printf("1-Soma\n");
        printf("2-Subtracao\n");
        printf("3-Divisao\n");
        printf("4-Multiplicacao\n");
        printf("5-Finalizar\n");
        printf("----------------\n");
        printf("Qual sua escolha: ");
        scanf("%d", &escolha);
        
        if(escolha == 5){
            exit(0);
        }
        else{
            if(escolha < 1 || escolha > 5){
                printf("Escolha Invalida\n");
                system("pause");
                system("cls");
            }
            else{
                printf("Informe os Valores\n");
                printf("Qual o primeiro valor: ");
                scanf("%f", &valor1);
                printf("Qual o segundo valor: ");
                scanf("%f", &valor2);

                if (escolha == 1){
                    soma = valor1 + valor2;
                    printf("A Soma de %f + %f = %f", valor1, valor2, soma);
                    system("pause");
                    system("cls");
                }
                else if (escolha == 2){
                    sub = valor1 - valor2;
                    printf("A Subtraçao de %f - %f = %f", valor1, valor2, sub);
                    system("pause");
                    system("cls");
                }
                else if (escolha == 3){
                    if (valor2 == 0){
                        printf("Impossivel a divisao por 0");
                        system("pause");
                        system("cls");
                    }
                    else{
                        div = valor1 / valor2;
                        printf("A divisao de %f / %f = %f", valor1, valor2, div);
                        system("pause");
                        system("cls");
                    }
                }
                else if (escolha == 4){
                    mult = valor1 * valor2;
                    printf("A multiplicacao de %f X %f = %f", valor1, valor2, mult);
                }
                
                
            }
        }
    }
}