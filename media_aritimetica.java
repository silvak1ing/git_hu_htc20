public class media_aritimetica {
    public static void main(String[] args) {
        double media1 = (8 + 9 + 7) / 3.0;
        double media2 = (4 + 5 + 6) / 3.0;
        double somaDasMedias = media1 + media2;
        double mediaDasMedias = somaDasMedias / 2;
        
        System.out.printf("Média dos números 8, 9 e 7: %.2f\n", media1);
        System.out.printf("Média dos números 4, 5 e 6: %.2f\n", media2);
        System.out.printf("Soma das duas médias: %.2f\n", somaDasMedias);
        System.out.printf("Média das médias: %.2f\n", mediaDasMedias);
    }
}

