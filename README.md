# Espelho de Emoji 🎭

Projeto de Visão Computacional que detecta expressões faciais via webcam e renderiza emojis correspondentes em tempo real.

## Estrutura do Projeto

```text
visao_computacional/
├── assets/
│   └── emojis/          # Imagens PNG com fundo transparente para cada emoção
├── src/
│   ├── __init__.py
│   ├── config.py        # Mapeamentos e constantes (câmera, nomes dos emojis)
│   ├── detector.py      # Lógica de detecção de expressões faciais (FER)
│   └── overlay.py       # Lógica para sobreposição de emojis sobre o vídeo
├── venv/                # Ambiente virtual Python
├── .gitignore           # Arquivos ignorados pelo Git
├── main.py              # Ponto de entrada do script (loop da webcam)
├── README.md            # Documentação de uso
└── requirements.txt     # Dependências do projeto
```

## Como Usar

### 1. Ativar o Ambiente Virtual (`venv`)

No terminal (PowerShell no Windows):
```powershell
.\venv\Scripts\Activate.ps1
```

*(Ou no Command Prompt `cmd`)*:
```cmd
venv\Scripts\activate.bat
```

### 2. Instalar as Dependências

Com o ambiente ativado, execute:
```bash
pip install -r requirements.txt
```

### 3. Adicionar os Emojis

Adicione imagens PNG (preferencialmente com canal alfa / transparência) na pasta `assets/emojis/` com os nomes correspondentes:
- `happy.png`
- `sad.png`
- `angry.png`
- `surprise.png`
- `fear.png`
- `disgust.png`
- `neutral.png`

### 4. Executar

Após implementar a lógica em `main.py` e nos módulos de `src/`:
```bash
python main.py
```
