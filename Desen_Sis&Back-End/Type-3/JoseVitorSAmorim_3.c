#include <stdio.h>
#include <ctype.h>
#include <string.h>

void imprimirMoeda(const char* texto, float valor) {
    char buffer[50];
    sprintf(buffer, "%.2f", valor); 
    
    for(int i = 0; buffer[i] != '\0'; i++) {
        if(buffer[i] == '.') {
            buffer[i] = ',';
        }
    }
    printf("%s%s\n", texto, buffer);
}

int main() {
    float valor_original = 0, desconto = 0, valor_montante = 0, desconto_vip = 0;
    char vip;

    while (1) {
        printf("Valor da compra: R$");
        scanf("%f", &valor_original);

        printf("Cliente VIP[S/N]: ");
        scanf(" %c", &vip);
        vip = toupper(vip);

        if (valor_original >= 500) {
            desconto = valor_original * 0.1;
            valor_montante = valor_original - desconto;
            if (vip == 'S') {
                desconto_vip = valor_montante * 0.05;
                valor_montante -= desconto_vip;
            }
            break;
        } 
        else if (valor_original < 500 && valor_original > 0) {
            desconto = valor_original * 0.05;
            valor_montante = valor_original - desconto;
            if (vip == 'S') {
                desconto_vip = valor_montante * 0.05;
                valor_montante -= desconto_vip;
            }
            break;
        } 
        else {
            printf("\033[31mCalma ai patrao, tem algo errado\033[m\n");
            printf("\033[33mTente novamente\033[m\n");
        }
    }

    printf("\n---Recibo de compra---\n");
    
    imprimirMoeda("Valor original: R$", valor_original);
    
    if (vip == 'S') {
        imprimirMoeda("Desconto: R$", desconto + desconto_vip);
    } 
    else {
        imprimirMoeda("Desconto: R$", desconto);
    }
    
    imprimirMoeda("Valor final: R$", valor_montante);
    int tamanho = strlen("---Recibo de compra---");
    for(int i = 0; i < tamanho; i++) {
        printf("-");
    }
    printf("\n");

    return 0;
}