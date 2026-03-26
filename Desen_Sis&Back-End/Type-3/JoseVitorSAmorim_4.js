const prompt = require('prompt-sync')();
const titulo = "Calculadora de IRPF 2026";

function linhas() {
    console.log("-".repeat(titulo.length));
}
function traco() {
    console.log("~".repeat(titulo.length));
}

function IRPF2026(salario_bruto) {
    linhas();
    const desconto_simples = 607.20;
    let inss = 0;
    if (salario_bruto <= 1500) {
        inss = salario_bruto * 0.075;
    } else if (salario_bruto <= 2800) {
        inss = salario_bruto * 0.09;
    } else if (salario_bruto <= 4000) {
        inss = salario_bruto * 0.12;
    } else {
        inss = 929.59;
    }
    const base_calculo = salario_bruto - desconto_simples;
    let aliquota = 0;
    let parcela_deduzir = 0;
    if (base_calculo <= 2428.80) {
        aliquota = 0;
        parcela_deduzir = 0;
    } else if (base_calculo <= 2826.65) {
        aliquota = 0.075;
        parcela_deduzir = 182.16;
    } else if (base_calculo <= 3751.05) {
        aliquota = 0.15;
        parcela_deduzir = 394.16;
    } else if (base_calculo <= 4664.68) {
        aliquota = 0.225;
        parcela_deduzir = 675.49;
    } else {
        aliquota = 0.275;
        parcela_deduzir = 988.73;
    }
    const imposto_base = (base_calculo * aliquota) - parcela_deduzir;
    let redutor_especial = 0;
    if (salario_bruto <= 5000) {
        redutor_especial = imposto_base;
    } else if (salario_bruto > 5000 && salario_bruto <= 7350) {
        redutor_especial = 978.62 - (0.133145 * salario_bruto);
    } else {
        redutor_especial = 0;
    }
    const imposto_final = Math.max(0, imposto_base - redutor_especial);
    const salario_liquido = salario_bruto - inss - imposto_final;
    return {
        "Salário Bruto": salario_bruto,
        "INSS": inss,
        "Base de Cálculo": base_calculo,
        "Alíquota": aliquota,
        "Parcela a Deduzir": parcela_deduzir,
        "Imposto Base": imposto_base,
        "Redutor Especial": redutor_especial,
        "Imposto Final": imposto_final,
        "Salário Líquido": salario_liquido
    };
}

traco();
console.log(titulo);
traco();
const input = prompt("Digite o salário bruto: ");
const salario = parseFloat(input.replace(',', '.')); 
if (isNaN(salario)) {
    console.log("Valor inválido. Por favor, digite apenas números.");
} else {
    const resultado = IRPF2026(salario);
    for (const [chave, valor] of Object.entries(resultado)) {
        console.log(`${chave}: R$${valor.toFixed(2)}`);
    }
}
linhas();