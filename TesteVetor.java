import java.util.Scanner;

public class TesteVetor {
    public static void main(String[] args) {
        boolean continuar = true;
        Scanner scanner = new Scanner(System.in);

        while (continuar) {
            System.out.print("Qual o tamanho do vetor? ");
            int tamanhoVetor = scanner.nextInt();

            NossoVetor vetor = new NossoVetor(tamanhoVetor);
            vetor.preencheVetor();

            System.out.println("Escolha uma opção:");
            System.out.println("1 - Bubble Sort");
            System.out.println("2 - Selection Sort");
            System.out.println("3 - Insertion Sort");
            System.out.println("4 - Busca Linear");
            System.out.println("5 - Busca Binária (exige vetor ordenado)");
            System.out.println("0 - Sair");
            System.out.print("Opção: ");
            int opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println(vetor.bubbleSort());
                    break;
                case 2:
                    System.out.println(vetor.selectionSort());
                    break;
                case 3:
                    System.out.println(vetor.insertionSort());
                    break;
                case 4: {
                    System.out.print("Qual número deseja buscar? ");
                    int num = scanner.nextInt();
                    System.out.println(vetor.buscaLinear(num));
                    break;
                }
                case 5: {
                    vetor.selectionSort(); // ordena antes de buscar
                    System.out.print("Qual número deseja buscar? ");
                    int num = scanner.nextInt();
                    System.out.println(vetor.buscaBinaria(num));
                    break;
                }
                case 0:
                    continuar = false;
                    break;
                default:
                    System.out.println("Opção inválida!");
            }

            if (opcao != 0) {
                System.out.print("Deseja realizar outra operação? (s/n): ");
                char resposta = scanner.next().toLowerCase().charAt(0);
                if (resposta != 's') {
                    continuar = false;
                }
            }
        }

        System.out.println("Programa encerrado.");
        scanner.close();
    }
}
