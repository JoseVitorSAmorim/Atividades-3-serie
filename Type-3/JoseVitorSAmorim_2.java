import java.util.Scanner;
public class JoseVitorSAmorim_2 {
    public static void main(String[] args) throws InterruptedException {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Nome: ");
            String nome = scanner.nextLine();
            System.out.print("Velocidade permitida: ");
            float velocidadePermitida = scanner.nextFloat();
            System.out.print("Velocidade real: ");
            float velocidadeReal = scanner.nextFloat();
            if (velocidadePermitida > 0 && velocidadeReal > 0) {
                float percentual = ((velocidadeReal - velocidadePermitida) / velocidadePermitida) * 100;

                if (velocidadeReal <= velocidadePermitida) {
                    System.out.println(nome + " não receberá multa");
                }
                else if (percentual <= 20) {
                    System.out.println(nome + " receberá multa leve");
                } 
                else if (percentual <= 50) {
                    System.out.println(nome + " receberá multa grave");
                } 
                else {
                    System.out.println(nome + " receberá multa gravíssima");
                }
            } 
            else {
                System.out.println("\033[31mCalma ai patrão, tem algo errado\033[m");
                System.out.println("\033[33mTente novamente\033[m");
                System.out.println("-".repeat(30));
            }
            scanner.nextLine();
            System.out.print("Deseja continuar[S/N]: ");
            String opcao = scanner.nextLine().toUpperCase();
            if (opcao.equals("N")) {
                break;
            }
        }
        System.out.println("\033[33mFinalizando o programa...\033[m");
        Thread.sleep(2000);
        System.out.println("\033[32mObrigado por usar nosso sistema\033[m");
        scanner.close();
    }
}
