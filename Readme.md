# Simulador de Fractal

Este projeto demonstra como a **Álgebra Linear** (transformações afins e recursão) pode ser utilizada para gerar fractais. Três fractais distintos são construídos:

1. **Samambaia de Barnsley**  
2. **Curva de Koch**  
3. **Triângulo de Sierpinski**  

Cada fractal é exibido com uma **animação** que mostra passo a passo o surgimento de suas formas.

---

## Descrição Geral

### 1) Samambaia de Barnsley

- **IFS (Sistema de Funções Iteradas)** de quatro transformações lineares afins, cada uma com uma probabilidade associada.  
- A cada iteração, um ponto é transformado multiplicando-se por uma matriz \(2 \times 2\) e somando-se um vetor de translação.  
- O conjunto desses pontos gera o desenho característico da Samambaia de Barnsley.

### 2) Curva de Koch

- **Fractal recursivo** em que cada segmento de reta é dividido em três partes iguais.  
- O segmento do meio é “levantado” para formar um triângulo, criando quatro novos segmentos.  
- Repetindo essa divisão recursiva em cada iteração, a curva vai ganhando cada vez mais detalhes.

### 3) Triângulo de Sierpinski (IFS Aleatório)

- Usamos um **método aleatório**: começamos com um ponto inicial e, a cada passo, escolhemos aleatoriamente um dos vértices de um triângulo (A, B ou C).  
- O novo ponto é o **ponto médio** entre o ponto atual e esse vértice.  
- Repetindo milhares de vezes, os pontos convergem para o Triângulo de Sierpinski.

---

## Requisitos

- Python 3.x  
- Bibliotecas:  
  - [NumPy](https://numpy.org/install/)  
  - [Matplotlib](https://matplotlib.org/stable/users/installing.html)

Exemplo de instalação via `pip`:
```bash
pip install numpy matplotlib
```

---

## Como Executar

1. **Baixe ou copie** o arquivo `.py` que contém o código dos três fractais.
2. **Abra o terminal** (ou prompt de comando) na pasta onde o arquivo está localizado.
3. **Execute**:
   ```bash
   python nome_do_arquivo.py
   ```
4. Serão abertas **três janelas** (uma após a outra), cada qual exibindo a animação de um fractal:
   - Janela 1: Samambaia de Barnsley  
   - Janela 2: Curva de Koch  
   - Janela 3: Triângulo de Sierpinski  

   Feche a janela atual para a próxima aparecer.

---

## Ajustes na Animação

- Cada animação possui parâmetros como `frames` e `interval` em `FuncAnimation`.  
  - **`frames`**: quantos estágios (quadros) serão mostrados até o fractal final.  
  - **`interval`** (em milissegundos): tempo de pausa entre cada quadro. Aumentar este valor torna a animação mais lenta.

- Para alterar a quantidade de pontos desenhados (ou o nível de detalhe nos fractais), verifique variáveis como `num_points`, `max_depth` e `total_frames` dentro de cada função.

---

## Estrutura Principal do Código

- **Funções auxiliares** para aplicar transformações, escolher transformações aleatórias e construir o fractal.
- **Três funções** que criam e animam cada fractal separadamente:
  1. `animate_barnsley()`
  2. `animate_koch()`
  3. `animate_sierpinski()`
- Ao final, cada função é chamada em sequência, com um `plt.show()` individual.

---

## Licença

Este projeto não possui uma licença específica integrada. Fique à vontade para utilizar e adaptar o código conforme necessário para fins de estudo ou experimentos pessoais.

---

## Créditos

- **Samambaia de Barnsley**: Inspirada no sistema de transformações descrito por Michael Barnsley.  
- **Curva de Koch**: Desenvolvida por Helge von Koch em 1904.  
- **Triângulo de Sierpinski**: Concebido pelo matemático Wacław Sierpiński em 1915.

Boa exploração e bons estudos!
