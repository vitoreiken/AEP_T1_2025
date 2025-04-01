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

    public long bubbleSort() {
        long contadorBS = 0;
        for (int i = 1; i < vetor.length; i++) {
            for (int j = 0; j < vetor.length - i; j++) {
                if (vetor[j] > vetor[j + 1]) {
                    int aux = vetor[j];
                    vetor[j] = vetor[j + 1];
                    vetor[j + 1] = aux;

                    contadorBS++;
                }
                contadorComparacaoBS++;
            }
        }
        return contadorBS;
    }

    public long selectionSort() {
        long contadorSS = 0;
        for (int i = 0; i < vetor.length - 1; ++i) {
            int min = i;
            for (int j = i + 1; j < vetor.length; ++j) {
                if (vetor[j] < vetor[min]) {
                    min = j;
                }
                int x = vetor[i];
                vetor[i] = vetor[min];
                vetor[min] = x;
                if (vetor[i] != vetor[min]) {
                    contadorSS++;
                }


            }
            int temp = vetor[min];
            vetor[min] = vetor[i];
            vetor[i] = temp;
            contadorTrocaSS += 3;
        }
        return contadorSS;
    }

    public long insertionSort() {
        long contadorIS = 0;
        for (int j = 1; j < vetor.length; ++j) {
            int x = vetor[j];
            int i;
            for (i = j - 1; i >= 0 && vetor[i] > x; --i) {
                vetor[i + 1] = vetor[i];
                contadorIS++;
            }
            vetor[i + 1] = x;
        }

        return contadorIS;
    }

    public int buscaLinear(int elemento) {
        int contadorLinear = 0;

        for (int i = 0; i < vetor.length; i++) {
            contadorLinear++;
            if (vetor[i] == elemento) {
                // System.out.println(i);
                return contadorLinear;

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
            contadorBinario++;
            if (elemento == vetor[meio]) {
                return contadorBinario;
            }
            contadorBinario++;

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
