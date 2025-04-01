// import java.util.Calendar;

import java.util.Random;

public class NossoVetor {

    private int[] vetor;
    private int ocupacao;

    public NossoVetor(int tamanho) {
        vetor = new int[tamanho];
        ocupacao = 0;
    }

    public boolean estaVazio() {
        return ocupacao == 0;
    }

    public void preencheVetor() {
        Random random = new Random();
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = random.nextInt(vetor.length * 1);

        }
        ocupacao = vetor.length;
    }

    public String bubbleSort() {
        long contadorTrocaBS = 0; // contador de trocas do BubbleSort
        long contadorComparacaoBS = 0; // contador de comparações do BubbleSort
        for (int i = 1; i < vetor.length; i++) {
            for (int j = 0; j < vetor.length - i; j++) {
                if (vetor[j] > vetor[j + 1]) {
                    int aux = vetor[j];
                    vetor[j] = vetor[j + 1];
                    vetor[j + 1] = aux;

                    contadorTrocaBS += 3;   
                }
                contadorComparacaoBS++;
            }
        }
        return "contador de trocas do bubbleSort: " + contadorTrocaBS + " || contador de comparação do bubbleSort: " + contadorComparacaoBS;
    }

    // {3, 9, 4, 1, 2, 6, 5, 8, 10, 7}
    public String selectionSort() {
        long contadorTrocaSS = 0, contadorComparacaoSS = 0;
        for (int i = 0; i < vetor.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < vetor.length; j++) {
                contadorComparacaoSS++;
                if (vetor[min] > vetor[j]) {
                    min = j;
                    contadorTrocaSS++;
                }
            }
            int temp = vetor[min];
            vetor[min] = vetor[i];
            vetor[i] = temp;
            contadorTrocaSS += 3;
        }
        return "contador de trocas do SelectionSort: " + contadorTrocaSS + " || contador de comparação do SelectionSort: " + contadorComparacaoSS;
    }

    // {3, 4, 9, 1, 2, 6, 5, 8, 10, 7}
    public String insertionSort() {
        long contadorTrocaIS = 0, contadorComparacaoIS = 0;
        for (int i = 1; i < vetor.length; i++) {
            int temp = vetor[i];
            int j = i - 1;
            while (j >= 0 && vetor[j] > temp) {
                vetor[j + 1] = vetor[j];
                j--;
                contadorTrocaIS++;
                contadorComparacaoIS++;
            }
            vetor[j + 1] = temp;
            contadorTrocaIS++;
        }
        return "contador de trocas do insertionSort: " + contadorTrocaIS + " || contador de comparação do insertionSort: " + contadorComparacaoIS;
    }

    public int buscaLinear(int elemento) {
        int contadorLinear = 0; // Contador de comparações

        for (int i = 0; i < vetor.length; i++) {
            if (vetor[i] == elemento) {
                // System.out.println(i); 

                contadorLinear++; 
            }
        }
        return contadorLinear;
    }

    public int buscaBinaria(int elemento) {
        int contadorBinario = 0; // Contador de comparações

        int inicio = 0;
        int fim = vetor.length - 1;
        while (inicio <= fim) {
            int meio = (inicio + fim) / 2;
            if (elemento == vetor[meio]) {
                // contadorBinario++;      //   CORRIGIR O LOCAL ONDE É APLICADO O CONTADOR!!
                return meio;
            }
            if (elemento > vetor[meio]) {
                inicio = meio + 1;
            } else {
                fim = meio - 1;
            }
        }
        return contadorBinario;
    }

    @Override
    public String toString() {
        String s = "ocupacao = " + ocupacao + "\n";
        for (int i = 0; i < ocupacao; i++) {
            s += vetor[i] + " ";
        }
        return s + "\n";
    }
}