# Organizador de Pastas - Python

Um script simples em **Python** que organiza automaticamente os arquivos de uma pasta, separando tudo por tipo (extensão).  
Ideal pra dar um fim na bagunça da pasta **Downloads**

---

## Funcionalidades

- Move arquivos automaticamente pra pastas baseadas em sua **extensão**.
- Cria as pastas de destino se elas **não existirem**.
- Suporte para os principais tipos de arquivos:
  - **Imagens:** `.jpg`, `.jpeg`, `.png`, `.gif`
  - **Documentos:** `.pdf`, `.docx`, `.txt`
  - **Compactados:** `.zip`, `.rar`
  - **Vídeos:** `.mp4`, `.mkv`, `.avi`
  - **Músicas:** `.mp3`, `.wav`
- Organização rápida e sem dor de cabeça — basta **executar o script**.

---

## Como Usar

1. **Baixe** o arquivo `organizador.py`.
2. Coloque o script **na pasta que deseja organizar**  
   *(ou altere o caminho dentro do código se quiser organizar outra pasta)*.
3. **Execute o script** de uma das formas:

### Opção 1 — Via Python
Abra o terminal (CMD) e digite:
```bash
python organizador.py

```

### Opção 2 — Com Arquivo .bat (2 cliques)

Crie um arquivo organizar.bat no mesmo local com o conteúdo:

**python organizador.py
pause**


Agora é só dar dois cliques e deixar o script fazer a mágica

---

### Exemplo de Organização

Antes:

Downloads/
├── imagem1.png
├── documento.pdf
├── musica.mp3
├── arquivo.zip


Depois:

Downloads/
├── Imagens/
│   └── imagem1.png
├── Documentos/
│   └── documento.pdf
├── Músicas/
│   └── musica.mp3
├── Compactados/
│   └── arquivo.zip

**Tecnologias Usadas**

Python 3.12.5

Módulos padrão: os, shutil



### Autor

**Filipe**

**Desenvolvedor Python | Freelancer
Contato: (filipeolima001@gmail.com)**

### Licença
Sem Licença.
