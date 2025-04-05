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
        long contadorComparacao = 0;
        long contadorTroca = 0;
        for (int i = 1; i < vetor.length; i++) {
            for (int j = 0; j < vetor.length - i; j++) {
                contadorComparacao++;
                if (vetor[j] > vetor[j + 1]) {
                    int aux = vetor[j];
                    vetor[j] = vetor[j + 1];
                    vetor[j + 1] = aux;

                    contadorTroca++;
                }
            }
        }
        return "Trocas: " + contadorTroca + "\nComparações: " + contadorComparacao;
    }

    public String selectionSort() {
        long contadorComparacao = 0;
        long contadorTroca = 0;
        for (int i = 0; i < vetor.length - 1; ++i) {
            int min = i;
            for (int j = i + 1; j < vetor.length; ++j) {
                contadorComparacao++;
                if (vetor[j] < vetor[min]) {
                    min = j;
                }
                int x = vetor[i];
                vetor[i] = vetor[min];
                vetor[min] = x;
                if (vetor[i] != vetor[min]) {
                    contadorTroca++;
                }

            }
        }
        return "Trocas: " + contadorTroca + "\nComparações: " + contadorComparacao;
    }

    public String insertionSort() {
        long contadorComparacao = 0;
        long contadorTroca = 0;
        for (int j = 1; j < vetor.length; ++j) {
            int x = vetor[j];
            int i = j-1;
            while(i >= 0) {
                contadorComparacao++;
                if(vetor[i] > x) {
                    vetor[i + 1] = vetor[i];
                    contadorTroca++;
                    i--;
                }
                else { 
                    break;
                }
            }
            vetor[i + 1] = x;
        }
        return "Trocas: " + contadorTroca + "\nComparações: " + contadorComparacao;
    }

    public String buscaLinear(int elemento) {
        long contadorComparacao = 0;

        for (int i = 0; i < vetor.length; i++) {
            contadorComparacao++;
            if (vetor[i] == elemento) {
                // System.out.println(i);
                return "Comparações: " + contadorComparacao;
            }
        }
        return "Comparações: " + contadorComparacao;
    }

    public String buscaBinaria(int elemento) {
        long contadorComparacao = 0; // Contador de comparações

        int inicio = 0;
        int fim = vetor.length - 1;
        while (inicio <= fim) {
            int meio = (inicio + fim) / 2;
            contadorComparacao++;
            if (elemento == vetor[meio]) {
                return "Comparaçoes: " + contadorComparacao;
            }

            if (elemento > vetor[meio]) {
                inicio = meio + 1;
            } else {
                fim = meio - 1;
            }
        }
        return "Comparações: " + contadorComparacao;
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
