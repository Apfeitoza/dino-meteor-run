# Dino Meteor Run 🦖☄️

Um jogo de sobrevivência e esquiva em estilo pixel art desenvolvido em Python utilizando a biblioteca **Pygame**. O projeto foi estruturado utilizando conceitos avançados de Engenharia de Software e Programação Orientada a Objetos (POO), servindo como trabalho final para a disciplina de Lógica de Programação Aplicada.

---

## 🎮 Conceito do Jogo

Inspirado nas clássicas mini-mecânicas de telas de carregamento de jogos retrô ( o mini-game da tela de loading do Grand Chase Mobile foi a inspiração para a gameplay), **Dino Meteor Run** coloca o jogador no controle de dinossauros que precisam correr o mais rápido possível para desviar de perigosos meteoros cadentes, enquanto coletam carnes para recuperar sua energia e pontuar.

---

## 🚀 Funcionalidades e Mecânicas Core

- **Seleção de Personagens Personalizados:** Quatro variações de dinossauros (**Doux, Mort, Tard e Vita**), cada um com atributos únicos de velocidade máxima e quantidade inicial de vida.
- **Mecânica de Movimentação e Dash:** Controles fluidos de locomoção lateral enriquecidos por um sistema de corrida (*Sneak/Dash*) acionado pela barra de espaço que duplica a velocidade atual.
- **Dificuldade Progressiva:** Um multiplicador de velocidade global (`speed_multiplier`) atua em tempo real, fazendo com que os meteoros caiam de forma mais rápida e agressiva à medida que os segundos avançam.
- **Condições Clássicas de Jogo:**
  - **Desafio:** Sobreviver ao bombardeio contínuo e imprevisível do céu.
  - **Condição de Vitória:** Resistir ao tempo limite estabelecido por nível (**Timeout de 60 segundos**).
  - **Condição de Derrota:** Perder todos os corações de vida antes do tempo acabar.
- **Persistência de Dados (Top 10 High Scores):** Integração com banco de dados relacional via **SQLite** com um painel integrado que exibe o ranking das dez pontuações mais altas registradas localmente.

---

## 🛠️ Arquitetura e Decisões Técnicas

O projeto foi totalmente refatorado com o objetivo de manter o código altamente desacoplado, limpo e preparado para uma futura portabilidade para ecossistemas Web modernos (como JavaScript/React).

- **Surface Virtual:** Implementação de uma camada gráfica intermediária (`display_surface`). Isso permite renderizar o jogo de forma pixel-perfect em uma resolução virtual interna estável (`GAME_WIDTH` e `GAME_HEIGHT`) e escalá-la responsivamente para a janela nativa do sistema (`WIN_WIDTH` e `WIN_HEIGHT`) sem distorcer as matrizes das artes originais ou gerar vazamentos em telas pretas.
- **Padrão de Projeto Factory (Fábrica de Entidades):** Centralização completa da inicialização física, carregamento de dicionários de animação dinâmicos (`load_frames`) e atribuição de estados através da classe `EntityFactory`, mantendo as classes finais focadas apenas nos seus comportamentos de locomoção.
- **Padrão de Projeto Mediator (Mediação de Estado):** O módulo `EntityMediator` atua de forma genérica e isolada filtrando e resolvendo todas as colisões de entidades (Meteoro vs Janela, Jogador vs Carne e Jogador vs Meteoros) gerenciando a matemática de dano, travas de teto de vida máxima (`min()`), incrementos de pontuação e disparos de triggers de efeitos visuais (`hurt_timer`).
- **Padrão Proxy de Banco de Dados:** O `DBProxy` gerencia as transações seguras de conexão e persistência de dados SQL, blindando o fluxo principal do loop do jogo de queries diretas.
- **Design de UI Consistente:** Substituição da renderização nativa de fontes do sistema operacional por um arquivo tipográfico embarcado (`PressStart2P-Regular.ttf`), garantindo portabilidade multiplataforma estável (macOS e Windows) sem quebras visuais de interface de usuário.

---

## 📁 Estrutura de Diretórios Principal

```text
├── DBScore                  # Banco de dados SQLite local
├── main.py                  # Ponto de entrada do sistema
├── requirements.txt         # Dependências do projeto (Pygame)
├── assets/                  # Todos os recursos binários do jogo
│   ├── font/                # Fontes TrueType embarcadas
│   ├── img/                 # Spritesheets organizados por estado/animação
│   └── music/               # Trilhas sonoras em .ogg e SFX estruturados
└── code/                    # Toda a lógica orientada a objetos (POO)
    ├── Const.py             # Configurações globais e centralização de volume
    ├── DBProxy.py           # Camada de comunicação SQL
    ├── EntityMediator.py    # Árbitro genérico de colisões e ciclo de vida
    ├── EntityFactory.py     # Gerenciador dinâmico de carregamento de assets
    └── ...                  # Classes de telas e objetos físicos
  ```
## 🎛️ Controles
- **Menus (Navegação):** - Setas Cima / Baixo / Esquerda / Direita para navegar pelas opções.

- **Enter / Space** para selecionar e confirmar.

- **ESC** para fechar e encerrar a aplicação com segurança.

- **Em Jogo:**

- **Seta Esquerda / Seta Direita para caminhar.**

- **Barra de Espaço + Seta para correr (Dash/Sneak).**

## 🔧 Como Executar Localmente
Pré-requisitos
Certifique-se de ter o Python 3.10+ instalado em sua máquina.

### 1. Ative seu ambiente virtual (venv):

- **No Windows:** `.venv\Scripts\activate`

- **No macOS/Linux:** `source .venv/bin/activate`

### 2. Instale as dependências:

```
pip install -r requirements.txt
```

### 3.Inicie o jogo a partir do arquivo raiz:
```
python main.py
```

Desenvolvido com 🦖, café e boas práticas de código.

Sprites dos dinos feitas pelo [Arks](https://arks.itch.io/dino-characters)
Sprites da carne e corações feitas por mim no Aseprite
Bgs do Craftpix
BGMS do pack do [Tallbeard](https://tallbeard.itch.io/music-loop-bundle)
Sfx criados no [Jfxr](https://jfxr.frozenfractal.com/)


## 💾 Download do Executável

Se você deseja apenas jogar o **Dino Meteor Run** sem precisar configurar o ambiente Python, você pode baixar o pacote pronto para Windows:

▶️ **[Clique aqui para baixar o jogo (.zip)](https://drive.google.com/drive/folders/15PuBwfd6GZnvnarG4aCYOoB-nNefsuUz?usp=drive_link)**

> ⚠️ **Nota de Execução:** Como o executável foi gerado de forma independente, o Windows SmartScreen pode exibir um alerta de segurança no primeiro lançamento. Se isso acontecer, clique em *"Mais informações"* e selecione *"Executar assim mesmo"*. Lembre-se de extrair todo o conteúdo do arquivo `.zip` antes de jogar para que a pasta `assets` seja lida corretamente!

