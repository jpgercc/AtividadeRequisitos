import java.util.ArrayList;
import java.util.Collections;

public class Timerer {
    private ArrayList<Double> tempos = new ArrayList<>();
    public long tempoInicial;
    private boolean contadorAtivo = false;

    public void iniciar() {
        tempos.clear();
        tempoInicial = System.currentTimeMillis();
        contadorAtivo = true;
    }

    public Double registrarTempo() {
        if (contadorAtivo) {
            long agora = System.currentTimeMillis();
            double tempoAtual = (agora - tempoInicial) / 1000.0;
            tempos.add(tempoAtual);
            tempoInicial = agora;
            return tempoAtual;
        }
        return null;
    }

    public ArrayList<Double> finalizar() {
        contadorAtivo = false;
        return tempos;
    }

    public double[] calcularEstatisticas() {
        if (!tempos.isEmpty()) {
            double media = tempos.stream().mapToDouble(Double::doubleValue).average().orElse(0);
            double maior = Collections.max(tempos);
            double menor = Collections.min(tempos);
            return new double[]{media, maior, menor};
        }
        return new double[]{0, 0, 0};
    }
}

//public double[] calcularEstatisticas() {
    //if (!tempos.isEmpty()) {
    //    double soma = 0;
      //  double maior = tempos.get(0);  // Inicializamos com o primeiro elemento
        //double menor = tempos.get(0);  // Inicializamos com o primeiro elemento

        // Iteramos sobre cada elemento em `tempos`
        //for (double tempo : tempos) {
            //soma += tempo;
          //  if (tempo > maior) {
            //    maior = tempo;
            //}
            //if (tempo < menor) {
              //  menor = tempo;
            //}
        //}

        // Calculamos a média dividindo a soma pelo número de elementos
        //double media = soma / tempos.size();
        //return new double[]{media, maior, menor};
    //}
    //return new double[]{0, 0, 0};  // Se a lista estiver vazia
//}
