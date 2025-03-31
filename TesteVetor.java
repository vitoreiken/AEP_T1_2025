import java.util.Scanner;

public class TesteVetor {
    public static void main(String[] args) {
        // NossoVetor vetorTeste = new NossoVetor(10);
        // vetorTeste.preencheVetor();
        // vetorTeste.bubbleSort();
        // System.out.println(vetorTeste.buscaLinear(7));
        // System.out.println(vetorTeste);
        Scanner scanner = new Scanner(System.in);
        NossoVetor vetorTeste;
        int t;
        int qtdTestes;

        System.out.println("Tamanho do Vetor: ");
        t = scanner.nextInt();
        System.out.println("Quantidade de Testes: ");
        qtdTestes = scanner.nextInt();

        for (int i = 1; i < qtdTestes + 1; i++) {
            vetorTeste = new NossoVetor(t);
            System.out.printf("\nBateria de Testes %d \n", i);

            vetorTeste.preencheVetor();
            System.out.println(vetorTeste.bubbleSort());

            vetorTeste.preencheVetor();
            System.out.println(vetorTeste.selectionSort());

            vetorTeste.preencheVetor();
            System.out.println(vetorTeste.insertionSort() + "\n");

        }
    }
}
