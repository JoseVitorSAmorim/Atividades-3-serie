public class Programa {
    public static void main(String[] args) {
        System.out.println("Meu nome completo é: Daniel Silva");

        int idade = 25;
        int ano = 2026;
        long populacao = 211049527L; 
        double distancia = 1000.5;   
        double altura = 1.78;        
        double salario = 5000.00;    
        char inicialNome = 'D';      
        boolean matriculado = true;  

        System.out.println("Idade: " + idade);
        System.out.println("Ano: " + ano);
        System.out.println("População: " + populacao);
        System.out.println("Distância: " + distancia + " km");
        System.out.println("Altura: " + altura + " metros");
        System.out.println("Salário: R$" + String.format("%.2f", salario));
        System.out.println("Inicial do nome: " + inicialNome);
        System.out.println("Matriculado: " + matriculado);
    }
}