import java.util.Scanner;
public class JoseVitorSAmorim_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        float valorOriginal = 0, desconto = 0, valorMontante = 0, descontoVip = 0;
        String vip = "";
        while (true) {
            System.out.print("Valor da compra: R$");
            valorOriginal = scanner.nextFloat();
            System.out.print("Cliente VIP[S/N]: ");
            vip = scanner.next().toUpperCase();
            if (valorOriginal >= 500) {
                desconto = (float) (valorOriginal * 0.1);
                valorMontante = valorOriginal - desconto;
                if (vip.equals("S")) {
                    descontoVip = (float) (valorMontante * 0.05);
                    valorMontante -= descontoVip;
                }
                break;
            } 
            else if (valorOriginal < 500 && valorOriginal > 0) {
                desconto = (float) (valorOriginal * 0.05);
                valorMontante = valorOriginal - desconto;
                if (vip.equals("S")) {
                    descontoVip = (float) (valorMontante * 0.05);
                    valorMontante -= descontoVip;
                }
                break;
            } 
            else {
                System.out.println("\033[31mCalma ai patrão, tem algo errado\033[m");
                System.out.println("\033[33mTente novamente\033[m");
            }
        }
        System.out.println("\n---Recibo de compra---");
        System.out.println("Valor original: R$" + String.format("%.2f", valorOriginal).replace(".", ","));
        if (vip.equals("S")) {
            System.out.println("Desconto: R$" + String.format("%.2f", desconto + descontoVip).replace(".", ","));
        } 
        else {
            System.out.println("Desconto: R$" + String.format("%.2f", desconto).replace(".", ","));
        }
        System.out.println("Valor final: R$" + String.format("%.2f", valorMontante).replace(".", ","));
        System.out.println("-".repeat("---Recibo de compra---".length()));
        scanner.close();
    }
}
