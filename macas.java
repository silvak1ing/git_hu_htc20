import java.util.Scanner;

public class macas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o número de maçãs compradas: ");
        int quantidade = scanner.nextInt();
        
        double preco = (quantidade < 12) ? 0.30 : 0.25;
        double total = quantidade * preco;
        
        System.out.printf("Valor total da compra: R$ %.2f\n", total);
        
        scanner.close();
    }
}

