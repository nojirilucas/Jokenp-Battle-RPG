# Jokenpô Battle RPG

<div align="center">
  <img src="https://github.com/user-attachments/assets/ec28d266-86e1-45f6-8f78-8a695ef2bc15" width="500" alt="Gameplay" />
  <p><i>Mini-game de combate por turnos em Python/Tkinter.</i></p>
</div>

## Descrição
Jogo desenvolvido como tarefa prática para o curso **Python Pro**, utilizando interfaces gráficas e lógica funcional. O objetivo é demonstrar o uso de bibliotecas integradas do Python para criar uma experiência interativa e visual.

---

## Compatibilidade por Sistema
O **Tkinter** é a biblioteca padrão do Python, mas sua instalação varia conforme o sistema operacional:

| Sistema | Como Garantir o Funcionamento |
| :--- | :--- |
| **Windows** | Geralmente já incluso na instalação padrão do Python. |
| **macOS** | Incluso no Python (pode exigir Tcl/Tk em versões antigas). |
| **Linux** | Requer instalação manual do pacote gráfico via terminal. |
| **WSL (Linux no Windows)** | **Não recomendado.** Exige um Servidor X. Use o PowerShell do Windows. |

---

## Como Executar

### 1. Preparação dos Arquivos
Certifique-se de que os arquivos `hero.png` e `enemy.png` estão na mesma pasta que o script `meu_app.py`. O código possui tratamento de erro, mas as imagens são essenciais para a experiência completa.

### 2. Instalação (Apenas Linux/Ubuntu)
Caso esteja no Linux, instale o suporte gráfico antes de rodar:
```bash
sudo apt update
sudo apt install python3-tk

python meu_app.py
ou 
python3 meu_app.py
