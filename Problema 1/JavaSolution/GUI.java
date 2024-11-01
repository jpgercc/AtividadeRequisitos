import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class GUI {
    private JFrame frame = new JFrame("Registro de Tempos do Nadador");
    private JLabel labelTempo = new JLabel("Tempo: 0.00 segundos");
    private JLabel labelResultados = new JLabel();
    private JButton botaoIniciar = new JButton("Iniciar");
    private JButton botaoRegistrar = new JButton("Registrar Tempo");
    private Timerer timerer;
    private Timer timer;
    private int voltas = 0;

    public GUI(Timerer timerer) {
        this.timerer = timerer;
        configurarJanela();
        configurarAcoes();
    }

    private void configurarJanela() {
        frame.setSize(850, 250);
        frame.setLayout(new GridLayout(5, 1, 10, 10));
        //5 linhas, 1 coluna, 10 pixels de espaçamento horizontal e 10 pixels de espaçamento vertical
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.add(new JLabel("Pressione 'Iniciar' para começar o treino."));
        frame.add(botaoIniciar);
        frame.add(botaoRegistrar);
        frame.add(labelTempo);
        frame.add(labelResultados);

        botaoRegistrar.setEnabled(false);
        frame.setVisible(true);
    }

    private void configurarAcoes() {
        botaoIniciar.addActionListener(e -> iniciarTreino());
        botaoRegistrar.addActionListener(e -> registrarTempo());
        //e -> é uma expressão lambda que define um ActionListener.
    }

    private void iniciarTreino() {
        timerer.iniciar();
        voltas = 0;
        botaoIniciar.setEnabled(false);
        botaoRegistrar.setEnabled(true);
        labelResultados.setText("");

        timer = new Timer(100, e -> atualizarTempo());
        timer.start();
    }

    private void atualizarTempo() {
        double tempoAtual = (System.currentTimeMillis() - timerer.tempoInicial) / 1000.0;
        labelTempo.setText(String.format("Tempo: %.2f segundos", tempoAtual));
    }

    private void registrarTempo() {
        Double tempo = timerer.registrarTempo();
        if (tempo != null) {
            labelTempo.setText(String.format("Tempo da volta: %.2f segundos", tempo));
            if (++voltas == 10) finalizarTreino();
        }
    }

    private void finalizarTreino() {
        labelTempo.setText("Treino finalizado!");
        botaoRegistrar.setEnabled(false);
        botaoIniciar.setEnabled(true);
        timer.stop();

        ArrayList<Double> tempos = timerer.finalizar();
        double[] stats = timerer.calcularEstatisticas();
        String resultados = String.format(
            "Tempos:  %s / Média: %.2f s Maior: %.2f s Menor: %.2f s", //o que é %s? r:
            tempos.toString().replaceAll("[\\[\\]]", ""), stats[0], stats[1], stats[2] //como posso fazer para que não exiba os colchetes?
        );
        labelResultados.setText(resultados);
    }
}
