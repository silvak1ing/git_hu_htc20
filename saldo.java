import java.util.Scanner;

public class saldo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Informe o saldo: ");
        double saldo = scanner.nextDouble();
        
        saldo *= 1.01;
        
        System.out.printf("Saldo com reajuste de 1%%: R$ %.2f\n", saldo);
        
        scanner.close();
    }
}

