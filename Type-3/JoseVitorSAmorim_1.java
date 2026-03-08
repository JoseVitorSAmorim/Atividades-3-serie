import java.util.Scanner;
public class JoseVitorSAmorim_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nome: ");
        String nome = scanner.nextLine();
        System.out.print("Nota: ");
        float nota = scanner.nextFloat();
        System.out.print("Presenca(%): ");
        int presenca = scanner.nextInt();
        if (presenca >= 50 && nota >= 80) {
            System.out.println("Aluno " + nome + " aprovado");
        } 
        else if (presenca >= 75 && nota >= 60) {
            System.out.println("Aluno " + nome + " aprovado");
        } 
        else {
            System.out.println("Aluno " + nome + " reprovado");
        }
    }
}
