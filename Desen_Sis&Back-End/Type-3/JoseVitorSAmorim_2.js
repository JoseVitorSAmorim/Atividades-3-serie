const prompt = require('prompt-sync')();
while (true) {
    let nome = prompt('Nome: ');
    let velocidade_permitida = parseFloat(prompt('Velocidade Permitida: '));
    let velocidade_real = parseFloat(prompt('Velocidade Real: '));
    if (velocidade_permitida>0 && velocidade_real>0) {
        let percentual = (velocidade_real - velocidade_permitida) / velocidade_permitida * 100;
        if (velocidade_real <= velocidade_permitida) {
            console.log(nome + ' não receberá multa.');
        }
        else if (percentual <= 20) {
            console.log(nome + ' receberá multa leve.');
        }
        else if (percentual <= 50) {
            console.log(nome + ' receberá multa grave.');
        }
        else if (percentual > 50) {
            console.log(nome + ' receberá multa gravíssima.');
        }
    }
    else {
        console.log('Calma ai patrão, tem algo errado.');
        console.log('Tente novamente.');
        console.log('-'.repeat(30));
    }
    let opcao = prompt('Deseja continuar[S/N]? : '.toLowerCase());
    if (opcao !== 's') {
        break;
    }
}
console.log('-'.repeat(30));
console.log('Programa encerrado.');