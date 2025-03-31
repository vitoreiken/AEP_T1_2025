public class TesteVetor {
    public static void main(String[] args) {
        NossoVetor vetorTeste = new NossoVetor(10);
        
        vetorTeste.preencheVetor();
        vetorTeste.bubbleSort();
        System.out.println(vetorTeste.buscaLinear(7));
        System.out.println(vetorTeste);
        // NossoVetor vetor100m = new NossoVetor(100000);
        // NossoVetor vetor200m = new NossoVetor(200000);
        // NossoVetor vetor400m = new NossoVetor(400000);
        // NossoVetor vetor800m = new NossoVetor(800000);
        // NossoVetor vetor16M = new NossoVetor(1600000);
    }
}
