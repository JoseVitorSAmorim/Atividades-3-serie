#include <stdio.h>

int main(){

    printf("Meu nome completo é José Vitor\n");

    int idade = 17;
    int ano = 2026;
    long populacao = 100000;
    float distancia = 100;
    float altura = 1.81;
    double salario = 1500.00;
    char inicial = 'J';
    int matricula = 7;

    printf("Idade: %d\n",idade);
    printf("Ano: %d\n",ano);
    printf("População: %ld\n",populacao);
    printf("Distancia: %.2f km\n",distancia);
    printf("Altura: %.2f\n",altura);
    printf("Salário: R$%.2lf\n",salario);
    printf("Inicial do nome: %c\n",inicial);
    printf("Matricula: %d\n",matricula);

    return 0;
}