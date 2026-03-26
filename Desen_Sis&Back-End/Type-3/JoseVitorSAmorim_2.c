#include <stdio.h>
#include <string.h>
#include <ctype.h> 
#include <windows.h> 

int main() {
    char nome[100];
    float velocidade_permitida, velocidade_real, percentual;
    char opcao;

    while (1) {
        printf("Nome: ");
        scanf(" %99[^\n]", nome);
        printf("Velocidade permitida: ");
        scanf("%f", &velocidade_permitida);
        printf("Velocidade real: ");
        scanf("%f", &velocidade_real);
        if (velocidade_permitida > 0 && velocidade_real > 0) {
            percentual = ((velocidade_real - velocidade_permitida) / velocidade_permitida) * 100;

            if (velocidade_real <= velocidade_permitida) {
                printf("%s nao recebera multa\n", nome);
            } 
            else if (percentual <= 20) {
                printf("%s recebera multa leve\n", nome);
            } 
            else if (percentual <= 50) {
                printf("%s recebera multa grave\n", nome);
            } 
            else {
                printf("%s recebera multa gravissima\n", nome);
            }
        } else {
            printf("\033[31mCalma ai patrao, tem algo errado\033[m\n");
            printf("\033[33mTente novamente\033[m\n");
            printf("------------------------------\n");
        }
        printf("Deseja continuar[S/N]: ");
        scanf(" %c", &opcao);
        opcao = toupper(opcao);
        if (opcao == 'N') {
            break;
        }
    }
    printf("\033[33mFinalizando o programa...\033[m\n");
    sleep(2);
    printf("\033[32mObrigado por usar nosso sistema\033[m\n");

    return 0;
}