import streamlit as st
import time
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="IFFluminense Campus Macaé")

with st.sidebar:

    with st.spinner("Carregando..."):
        time.sleep(3)
    st.image("./IF.png")
    st.markdown(
        """Trabalho apresentado ao Curso Integrado de Eletrônica do IFFLUMINENSE – Instituto Federal de Educação, Ciência e Tecnologia Fluminense – Campus MACAÉ  
    para as disciplinas de: Matemática  
    Professora: Izabela"""
    )
    st.success("Seminário arregado com sucesso!")

st.title("FUNÇÃO POLINOMIAL DO 1º GRAU")

tab1, tab3, tab4 = st.tabs(["📝 Teoria", "⚡ Eletrônica", "📟 Osciloscópio"])

with tab1:
    st.title("Função Afim")

   
    st.write("""A **função afim** é uma função matemática da forma: f(x) = ax + b, onde: (a) é o coeficiente angular, que determina a inclinação da reta; (b) é o coeficiente linear, que representa o valor de f(x) quando x = 0. A função afim é uma função linear, sendo sua representação gráfica uma reta. O coeficiente angular (a) pode ser positivo, negativo ou igual a zero, o que altera a direção e a inclinação da reta: Se (a > 0), a reta é crescente. Se (a < 0), a reta é decrescente. Se (a = 0), a reta é horizontal. Gráfico da Função Afim Para visualizar a função afim, você pode ajustar os coeficientes (a) e (b):""")

    
    a = st.slider("Coeficiente Angular (a)", -5, 5, 1, step=1)
    b = st.slider("Coeficiente Linear (b)", -10, 10, 0, step=1)

    x = np.arange(-10, 11, 1)  # Apenas inteiros de -10 a 10
    # Calcular os valores de y usando a função afim
    y = a * x + b

    # Criar o gráfico com Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers+lines', name='f(x) = {}x + {}'.format(a, b)))

    
    fig.update_layout(
        title="Gráfico da Função Afim",
        xaxis_title="x",
        yaxis_title="f(x)",
        template="plotly_dark",
        height=500
    )

    # Exibir o gráfico
    st.plotly_chart(fig)

with tab3:



    opcoes = ["Eletrônica Analógica", "Amplificadores Lineares", "Osciloscópios"]
    selecao = st.multiselect("Selecione o que deseja visualizar:", opcoes)

    # Introdução à Eletrônica Analógica
    if "Eletrônica Analógica" in selecao:
        st.header("Introdução à Eletrônica Analógica")
        st.write("""A eletrônica analógica é um ramo da eletrônica que lida com sinais contínuos e a manipulação desses sinais em circuitos que operam em níveis de tensão e corrente variáveis. Ao contrário da eletrônica digital, que se baseia em sinais discretos e lógicos, a eletrônica analógica é fundamental para o tratamento de informações que podem assumir um número infinito de valores. Esse tipo de eletrônica é amplamente utilizado em amplificadores, filtros, osciladores e circuitos de modulação, sendo essencial em diversas aplicações, como áudio, telecomunicações e instrumentação.""")

    #amplificadores lineares
    if "Amplificadores Lineares" in selecao:
        st.header("Amplificadores Lineares")
        st.write("""Os amplificadores lineares, dispositivos centrais da eletrônica analógica, são projetados para aumentar o sinal de entrada sem distorcer suas características fundamentais. Eles seguem o princípio da função afim \( y = ax + b \), onde \( x \) representa o sinal de entrada, \( a \) o ganho (que determina o quanto o sinal será amplificado) e \( b \) uma constante que pode representar um ajuste de offset no circuito. A linearidade desses amplificadores é crucial para garantir que o sinal de saída mantenha uma relação proporcional com o sinal de entrada, evitando distorções.""")

    #osciloscópios
    if "Osciloscópios" in selecao:
        st.header("Osciloscópios")
        st.write("""O osciloscópio é um instrumento fundamental na eletrônica analógica, permitindo a visualização e medição de sinais elétricos variáveis ao longo do tempo. Ele possibilita a observação da forma de onda de um sinal, sua amplitude, frequência e qualquer distorção presente. Quando conectado a um amplificador linear, o osciloscópio pode verificar a fidelidade da amplificação, evidenciando se a saída segue a mesma forma que a entrada e, portanto, se a relação entre ambos é linear, conforme a função afim \( y = ax + b \).""")

    # Conclusão
    if len(selecao) > 0:
        st.write("""Em síntese, a eletrônica analógica desempenha um papel crucial na manipulação de sinais contínuos, sendo os amplificadores lineares e osciloscópios ferramentas indispensáveis para garantir a qualidade e a integridade dos sinais em uma ampla gama de aplicações tecnológicas.""")

    
with tab4:
    t = np.linspace(0, 1, 500)  # vetor de tempo
    # Sliders para ajustar frequência, amplitude e ganho (apenas inteiros)
    freq = st.slider("Frequência (Hz)", 1, 10, 5, step=1)
    amplitude = st.slider("Amplitude", 1, 5, 1, step=1)
    gain = st.slider("Ganho", 1, 10, 2, step=1)

    # Cálculo da onda
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    amplified_wave = gain * wave  # Onda amplificada

    # Criar o gráfico
    fig = go.Figure()

    # onda original
    fig.add_trace(go.Scatter(x=t, y=wave, mode='lines', name='Sinal Original', line=dict(color='blue')))

    #onda amplificada
    fig.add_trace(go.Scatter(x=t, y=amplified_wave, mode='lines', name='Sinal Amplificado', line=dict(color='orange')))

    # layout se parecer com um osciloscópio
    fig.update_layout(
        title="Osciloscópio - Sinal Original e Amplificado",
        xaxis_title="Tempo (s)",
        yaxis_title="Amplitude",
        xaxis=dict(showgrid=True, zeroline=True),
        yaxis=dict(showgrid=True, zeroline=True),
        showlegend=False,
        height=500
    )

    # Adicionar marcadores de eixos y em inteiros
    y_tick_vals = np.arange(-gain * amplitude, gain * amplitude + 1, 1)
    fig.update_yaxes(tickvals=y_tick_vals)

    # Exibir o gráfico
    st.plotly_chart(fig)

    st.write("""Este simulador permite ajustar a frequência, a amplitude e o ganho de um sinal senoidal. A onda original é mostrada em azul, enquanto a onda amplificada é exibida em laranja. Experimente alterar os valores dos sliders para ver como isso afeta as ondas!""")

    st.write("""
    ### Onde o Amplificador Está Agindo?

    No gráfico, o amplificador está atuando diretamente sobre a **amplitude** do sinal senoidal. A onda azul representa o **sinal original**, cuja amplitude é controlada pelo valor selecionado no slider de 'Amplitude'. Já a onda laranja corresponde ao **sinal amplificado**, onde o valor do **ganho** multiplica a amplitude do sinal original.

    Assim, o amplificador está **escalando a amplitude** da onda original, sem modificar sua frequência ou forma. Quando o ganho é aumentado, a diferença entre o sinal original e o amplificado se torna mais visível, pois a amplitude da onda amplificada cresce proporcionalmente ao valor do ganho.

    Resumidamente, o amplificador modifica apenas a altura (ou intensidade) da onda, mantendo a frequência e o formato da oscilação inalterados. Quanto maior o ganho, maior será essa amplificação visualizada na onda laranja.
    """)
