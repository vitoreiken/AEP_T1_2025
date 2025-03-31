import java.util.Calendar;
import java.util.Random;

public class NossoVetor{
    private int[] vetor;
    private int ocupacao;
    
    public NossoVetor(int tamanho){
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

    public void bubbleSort(){
        for (int i=1; i<vetor.length; i++){
            for (int j=0; j<vetor.length-i; j++){
                if (vetor[j]>vetor[j+1]){
                    int aux = vetor[j];
                    vetor[j] = vetor[j+1];
                    vetor[j+1] = aux;
                }
            }
        }
    }

    public void selectionSort(){
        for (int i=0; i<vetor.length-1; ++i){
            int min = i;
            for (int j=i+1; j<vetor.length; ++j){
                if (vetor[j]<vetor[min])
                    min=j;
            int x = vetor[i];
            vetor[i] = vetor[min];
            vetor[min] = x;
            }
        }
    }

    public void insertionSort(){
        for (int j=1; j<vetor.length; ++j){
            int x = vetor[j];
            int i;
            for (i=j-1; i>=0&&vetor[i]>x; --i)
                vetor[i+1] = vetor[i];
            vetor[i+1]=x;
        }
    }

    public int buscaLinear(int elemento){
        for(int i = 0; i < ocupacao; i++){
            if(vetor[i] == elemento){
                return i;
            }
        }
        return -1;
    }
    
    public int buscaBinaria(int elemento){
        int inicio = 0;
        int fim = vetor.length;
        while (inicio<vetor[fim-1]){
            int meio = (inicio+fim)/2;
            if (vetor[meio]<elemento){
                inicio = meio;
            } else{
                fim = meio;
            }
        }
        return fim;
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