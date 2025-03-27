#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main(){
    float n1, n2, n3, n4, Media;
    printf("Digite a 1 Nota: ");
    scanf("%f", &n1);
    printf("Digite a 2 nota: ");
    scanf("%f", &n2);
    printf("Digite a 3 nota: ");
    scanf("%f", &n3);
    printf("Digite a 4 nota: ");
    scanf("%f", &n4);

    Media = (n1+n2+n3+n4)/4;
    if (Media >= 6)
        printf("\nAluno Aprovado!");
    else
        if (Media < 4)
            printf("\nAluno Reprovado!");
        else
            printf("\nAluno ficou de prova final");

    getche();
    return(0);
}