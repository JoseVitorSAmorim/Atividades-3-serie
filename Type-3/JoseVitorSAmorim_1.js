const prompt = require("prompt-sync")();
let nome = prompt("Nome: ");
let nota = prompt("Nota: ");
let presenca = prompt("Presença(%): ");
if (presenca >= 50 && nota >= 80) {
    console.log(nome + " foi aprovado!");
}
else if (presenca >= 75 && nota >= 60) {
    console.log(nome + " foi aprovado!");
}
else {    
    console.log(nome + " foi reprovado!");
}