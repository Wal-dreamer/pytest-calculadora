# Guia de Configuração do Projeto TDD

Como você mencionou que não tem muita experiência com programação, aqui está o passo a passo para configurar seu ambiente no VS Code:

## 1. Abrir a pasta no VS Code
Abra o VS Code e vá em `File > Open Folder...` e selecione a pasta `tdd_project`.

## 2. Criar o Ambiente Virtual (VENV)
O ambiente virtual serve para isolar as bibliotecas do seu projeto. No terminal do VS Code, digite:
```bash
python -m venv venv
```

## 3. Ativar o Ambiente Virtual
- **Windows:**
  ```powershell
  .\venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

## 4. Instalar o Pytest
Com o ambiente ativado (você verá um `(venv)` no início da linha do terminal), instale o framework de testes:
```bash
pip install pytest
```

## 5. Como ver os ciclos RED, GREEN e REFACTOR
Para ver os três ciclos acontecendo no seu terminal (exatamente como o professor pediu), eu criei um script de demonstração. 

No terminal do VS Code, com o ambiente ativado, digite:
```bash
python demonstrar_tdd.py
```
Este script irá:
1.  **Limpar o código** para mostrar o erro (**RED**).
2.  **Adicionar o código básico** para mostrar o sucesso (**GREEN**).
3.  **Melhorar o código** mantendo o sucesso (**REFACTOR**).

Basta seguir as instruções na tela e pressionar ENTER.

## 6. Estrutura de Arquivos
O projeto terá a seguinte estrutura:
- `calculadora.py`: Onde ficará a lógica do nosso código.
- `test_calculadora.py`: Onde ficarão os nossos testes.
