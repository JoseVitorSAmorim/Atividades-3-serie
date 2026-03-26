#include <stdio.h>

int main() {
    char nome[100];
    float nota;
    int presenca;
    
    printf("Nome: ");
    scanf(" %99[^\n]", nome);
    printf("Nota: ");
    scanf("%f", &nota);
    printf("Presenca(%%): ");
    scanf("%d", &presenca);
    if (presenca >= 50 && nota >= 80) {
        printf("Aluno %s aprovado\n", nome);
    } 
    else if (presenca >= 75 && nota >= 60) {
        printf("Aluno %s aprovado\n", nome);
    } 
    else {
        printf("Aluno %s reprovado\n", nome);
    }

    return 0;
}