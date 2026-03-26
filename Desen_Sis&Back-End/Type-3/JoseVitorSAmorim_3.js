const prompt = require('prompt-sync')();
let valor_original = 0;
let vip = '';
let desconto = 0;
let desconto_vip = 0;
let valor_montante = 0;

while (true) {
    valor_original = parseFloat(prompt('Valor da compra: R$'));
    vip = prompt('O cliente é VIP[S/N]? ').toUpperCase();
    
    if (valor_original >= 500) {
        desconto = valor_original * 0.1;
        valor_montante = valor_original - desconto;
        if (vip === 'S') {
            desconto_vip = valor_montante * 0.05;
            valor_montante -= desconto_vip;
        }
        break;
    }
    else if (valor_original < 500 && valor_original > 0) {
        desconto = valor_original * 0.05;
        valor_montante = valor_original - desconto;
        if (vip === 'S') {
            desconto_vip = valor_montante * 0.05;
            valor_montante -= desconto_vip;
        }
        break;
    }
    else {
        console.log('Calma ai patrão, tem algo errado.');
        console.log('Tente novamente.');
        console.log('-'.repeat(30));
    }
}
console.log('\n---Recibo de compra---');
console.log(`Valor original: R$${valor_original.toFixed(2)}`);
if (vip === 'S') {
    console.log('Desconto total: R$' + (desconto + desconto_vip).toFixed(2));
} else {
    console.log('Desconto: R$' + desconto.toFixed(2));
}
console.log('Valor final: R$' + valor_montante.toFixed(2));
console.log('-'.repeat('---Recibo de compra---'.length));