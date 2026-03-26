#include <stdio.h>
#include <string.h>
#include <math.h> 

const char titulo[] = "Calculadora de IRPF 2026";

typedef struct {
    float salario_bruto;
    float inss;
    float base_calculo;
    float aliquota;
    float parcela_deduzir;
    float imposto_base;
    float redutor_especial;
    float imposto_final;
    float salario_liquido;
} ResultadoIRPF;
void linhas() {
    for (int i = 0; i < strlen(titulo); i++) {
        printf("-");
    }
    printf("\n");
}
void traco() {
    for (int i = 0; i < strlen(titulo); i++) {
        printf("~");
    }
    printf("\n");
}

ResultadoIRPF calcularIRPF2026(float salario_bruto) {
    linhas();
    ResultadoIRPF res;
    float desconto_simples = 607.20;
    if (salario_bruto <= 1500) {
        res.inss = salario_bruto * 0.075;
    } 
    else if (salario_bruto <= 2800) {
        res.inss = salario_bruto * 0.09;
    } 
    else if (salario_bruto <= 4000) {
        res.inss = salario_bruto * 0.12;
    } 
    else {
        res.inss = 929.59;
    }
    res.base_calculo = salario_bruto - desconto_simples;
    if (res.base_calculo <= 2428.80) {
        res.aliquota = 0;
        res.parcela_deduzir = 0;
    } 
    else if (res.base_calculo <= 2826.65) {
        res.aliquota = 0.075;
        res.parcela_deduzir = 182.16;
    } 
    else if (res.base_calculo <= 3751.05) {
        res.aliquota = 0.15;
        res.parcela_deduzir = 394.16;
    } 
    else if (res.base_calculo <= 4664.68) {
        res.aliquota = 0.225;
        res.parcela_deduzir = 675.49;
    } 
    else {
        res.aliquota = 0.275;
        res.parcela_deduzir = 988.73;
    }
    res.imposto_base = (res.base_calculo * res.aliquota) - res.parcela_deduzir;
    if (salario_bruto <= 5000) {
        res.redutor_especial = res.imposto_base;
    } 
    else if (salario_bruto > 5000 && salario_bruto <= 7350) {
        res.redutor_especial = 978.62 - (0.133145 * salario_bruto);
    } 
    else {
        res.redutor_especial = 0;
    }
    res.imposto_final = fmax(0.0, res.imposto_base - res.redutor_especial);
    res.salario_liquido = salario_bruto - res.inss - res.imposto_final;
    res.salario_bruto = salario_bruto; // Guardando o original na struct
    return res;
}

int main() {
    traco();
    printf("%s\n", titulo);
    traco();
    float salario;
    printf("Digite o salario bruto: ");
    scanf("%f", &salario);
    ResultadoIRPF resultado = calcularIRPF2026(salario);
    printf("Salario Bruto: R$%.2f\n", resultado.salario_bruto);
    printf("INSS: R$%.2f\n", resultado.inss);
    printf("Base de Calculo: R$%.2f\n", resultado.base_calculo);
    printf("Aliquota: R$%.2f\n", resultado.aliquota);
    printf("Parcela a Deduzir: R$%.2f\n", resultado.parcela_deduzir);
    printf("Imposto Base: R$%.2f\n", resultado.imposto_base);
    printf("Redutor Especial: R$%.2f\n", resultado.redutor_especial);
    printf("Imposto Final: R$%.2f\n", resultado.imposto_final);
    printf("Salario Liquido: R$%.2f\n", resultado.salario_liquido);
    linhas();

    return 0;
}