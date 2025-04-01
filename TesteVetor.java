import java.util.Scanner;
public class TesteVetor {
    public static void main(String[] args) {
        // NossoVetor vetorTeste = new NossoVetor(10);
        // vetorTeste.preencheVetor();
        // vetorTeste.bubbleSort();
        // System.out.println(vetorTeste.buscaBinaria(7));
        // System.out.println(vetorTeste);

        Scanner scanner = new Scanner(System.in);
        NossoVetor vetorTeste;
        int t;
        int e;
        int qtdTestes;

        
        System.out.println("Tamanho do Vetor: "); // definir o tamanho do vetor
        t = scanner.nextInt();
        System.out.println("Elemento a ser buscado: "); // Definir elemento de busca
        e = scanner.nextInt();
        System.out.println("Quantidade de Testes: "); // 
        qtdTestes = scanner.nextInt();

        for (int i = 1; i < qtdTestes + 1; i++) {
            vetorTeste = new NossoVetor(t);
            System.out.printf("\nBateria de Testes %d \n", i);

            vetorTeste.preencheVetor();
            System.out.println(vetorTeste.buscaLinear(e));  // busca linear antes de ordenar o vetor
            System.out.println(vetorTeste.bubbleSort());
            System.out.println(vetorTeste.buscaBinaria(e) + "\n");   // busca binária depois de ordenar o valor 

            vetorTeste.preencheVetor();
            System.out.println(vetorTeste.buscaLinear(e));
            System.out.println(vetorTeste.selectionSort());
            System.out.println(vetorTeste.buscaBinaria(e) + "\n");

            vetorTeste.preencheVetor();
            System.out.println(vetorTeste.buscaLinear(e));
            System.out.println(vetorTeste.insertionSort());
            System.out.println(vetorTeste.buscaBinaria(e) + "\n");
        }

        scanner.close();

    }
}