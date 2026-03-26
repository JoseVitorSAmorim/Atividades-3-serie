import java.util.Scanner;
import java.util.LinkedHashMap;
import java.util.Map;
public class JoseVitorSAmorim_4 {
    static final String TITULO = "Calculadora de IRPF 2026";

    static void linhas() {
        System.out.println("-".repeat(TITULO.length()));
    }

    static void traco() {
        System.out.println("~".repeat(TITULO.length()));
    }

    static Map<String, Double> IRPF2026(double salarioBruto) {
        linhas();
        double descontoSimples = 607.20;
        double inss = 0;
        if (salarioBruto <= 1500) {
            inss = salarioBruto * 0.075;
        } 
        else if (salarioBruto <= 2800) {
            inss = salarioBruto * 0.09;
        } 
        else if (salarioBruto <= 4000) {
            inss = salarioBruto * 0.12;
        } 
        else {
            inss = 929.59;
        }

        double baseCalculo = salarioBruto - descontoSimples;
        double aliquota = 0;
        double parcelaDeduzir = 0;

        if (baseCalculo <= 2428.80) {
            aliquota = 0;
            parcelaDeduzir = 0;
        } 
        else if (baseCalculo <= 2826.65) {
            aliquota = 0.075;
            parcelaDeduzir = 182.16;
        } 
        else if (baseCalculo <= 3751.05) {
            aliquota = 0.15;
            parcelaDeduzir = 394.16;
        } 
        else if (baseCalculo <= 4664.68) {
            aliquota = 0.225;
            parcelaDeduzir = 675.49;
        } 
        else {
            aliquota = 0.275;
            parcelaDeduzir = 988.73;
        }

        double impostoBase = (baseCalculo * aliquota) - parcelaDeduzir;
        double redutorEspecial = 0;

        if (salarioBruto <= 5000) {
            redutorEspecial = impostoBase;
        } 
        else if (salarioBruto > 5000 && salarioBruto <= 7350) {
            redutorEspecial = 978.62 - (0.133145 * salarioBruto);
        } 
        else {
            redutorEspecial = 0;
        }

        double impostoFinal = Math.max(0, impostoBase - redutorEspecial);
        double salarioLiquido = salarioBruto - inss - impostoFinal;

        Map<String, Double> resultado = new LinkedHashMap<>();
        resultado.put("Salário Bruto", salarioBruto);
        resultado.put("INSS", inss);
        resultado.put("Base de Cálculo", baseCalculo);
        resultado.put("Alíquota", aliquota);
        resultado.put("Parcela a Deduzir", parcelaDeduzir);
        resultado.put("Imposto Base", impostoBase);
        resultado.put("Redutor Especial", redutorEspecial);
        resultado.put("Imposto Final", impostoFinal);
        resultado.put("Salário Líquido", salarioLiquido);

        return resultado;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        traco();
        System.out.println(TITULO);
        traco();
        System.out.print("Digite o salário bruto: ");
        double salario = scanner.nextDouble();
        Map<String, Double> resultado = IRPF2026(salario);
        for (Map.Entry<String, Double> item : resultado.entrySet()) {
            System.out.printf("%s: R$%.2f\n", item.getKey(), item.getValue());
        }
        linhas();
        scanner.close();
    }
}
