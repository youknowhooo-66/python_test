# Exemplos de Visão Computacional com OpenCV

Este repositório contém uma coleção de scripts Python demonstrando conceitos fundamentais de Visão Computacional utilizando a biblioteca OpenCV. É um excelente ponto de partida para quem está aprendendo a manipular imagens e vídeos programaticamente.

## 🚀 Como Começar

### Pré-requisitos

*   Python 3.x
*   Pip (gerenciador de pacotes do Python)

### Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-repositorio>
    cd python_test
    ```

2.  **Ative o ambiente virtual:**
    *   **Windows:**
        ```powershell
        .\python\.venv\Scripts\activate
        ```
    *   **Linux/macOS:**
        ```bash
        source python/.venv/bin/activate
        ```

3.  **Instale as dependências (caso não estejam instaladas):**
    ```bash
    pip install opencv-python numpy
    ```

## 📂 Estrutura do Projeto

A pasta contém os seguintes exemplos:

*   `01_carregar_imagem.py`: Como carregar e exibir uma imagem em uma janela.
*   `02_webcam.py`: Acesso e manipulação de fluxo de vídeo da webcam em tempo real.
*   `03_tons_de_cinza.py`: Conversão de imagens coloridas para escala de cinza.
*   `04_deteccao_bordas.py`: Aplicação do algoritmo Canny para detecção de bordas.
*   `05_desenhar_formas.py`: Como desenhar linhas, retângulos, círculos e texto em imagens.
*   `06_redimensionar_rotacionar.py`: Transformações geométricas básicas (redimensionamento e rotação).
*   `07_suavizacao_blur.py`: Técnicas de filtragem para redução de ruído (Blur, Gaussian Blur).
*   `08_deteccao_faces.py`: Exemplo básico de detecção facial usando classificadores Haar Cascade.
*   `09_segmentacao_cor.py`: Filtragem de cores específicas em uma imagem (espaço de cor HSV).
*   `10_contornos.py`: Identificação e desenho de contornos em objetos.

## 🛠️ Executando os Exemplos

Para rodar qualquer exemplo, execute o script desejado:

```bash
python 01_carregar_imagem.py
```

> **Nota:** Certifique-se de que o arquivo `imagem.jpg` esteja presente na pasta `python/` para que os scripts que dependem dele funcionem corretamente.
