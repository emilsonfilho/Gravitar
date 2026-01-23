# Gravitar 🌌

Simulador de gravidade N-Corpos (N-Body) desenvolvido em Python.

O projeto tem como objetivo simular a interação gravitacional entre múltiplos corpos celestes utilizando diferentes métodos de integração numérica, permitindo visualizar órbitas complexas e cenários clássicos da astrofísica.

## 🚀 Funcionalidades

* **Simulação N-Body:** Suporta qualquer número de corpos interagindo gravitacionalmente.
* **Cenários Configuráveis:** Carregamento de sistemas via arquivos JSON (ex: Sistema Solar, Pontos de Lagrange, Órbita em "Figura 8").
* **Múltiplos Integradores:**
    * **Euler:** Método de primeira ordem (básico).
    * **Symplectic (Semi-Implicit Euler):** Método que preserva melhor a energia do sistema a longo prazo, ideal para órbitas estáveis.
* **Visualização em Tempo Real:** Renderização das trajetórias utilizando Matplotlib.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Computação Científica:** NumPy
* **Visualização:** Matplotlib
* **Configuração:** JSON

## 📂 Estrutura do Projeto

A arquitetura foi desenhada para ser modular e extensível:

* `src/modules/physics/`: Lógica das forças gravitacionais.
* `src/modules/integration/`: Implementação dos algoritmos numéricos (Euler, Simplético).
* `src/modules/render/`: Gerenciamento da visualização gráfica.
* `config/`: Arquivos JSON com os parâmetros iniciais de cada simulação.

## 🎮 Como Executar

1.  Clone o repositório:
    ```bash
    git clone https://github.com/emilsonfilho/gravitar.git
    cd gravitar
    ```

2.  Instale as dependências (caso ainda não tenha):
    ```bash
    pip install numpy matplotlib
    ```

3.  Execute a simulação escolhendo um cenário (altere no código ou passe como argumento se implementado):
    ```bash
    python src/main.py
    ```

## 🌌 Cenários Disponíveis

O projeto já inclui diversas configurações prontas na pasta `config/`:

* **realSunEarth.json:** Simulação realista do sistema Terra-Sol.
* **figure8.json:** A famosa solução de três corpos em órbita de "oito".
* **lagrange.json:** Demonstração dos pontos de equilíbrio gravitacional.
* **perfect-circle.json:** Teste de estabilidade orbital.

---

Feito com ❤️ by **Emilson Filho**
