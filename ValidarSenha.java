import java.util.Scanner;

public class ValidarSenha {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int senha;
      
         int senhac = 1234;
        
        do {
            System.out.print("Digite a senha: ");
            senha = scanner.nextInt();
            
            if (senha != senhac) {
                System.out.println("ACESSO NEGADO");
            }
        } while (senha != senhac);
        
        System.out.println("ACESSO PERMITIDO");
        scanner.close();
    }
}

