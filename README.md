# Jokenpô Battle RPG

<div align="center">
  <img src="https://github.com/user-attachments/assets/ec28d266-86e1-45f6-8f78-8a695ef2bc15" width="500" alt="Gameplay do Jokenpô Battle RPG" />
  <p><i>Mini-game de combate por turnos inspirado em mecânicas clássicas de RPG.</i></p>
</div>

## Descrição
Este é um mini-game de combate por turnos desenvolvido em **Python** utilizando a biblioteca gráfica **Tkinter**. O jogador assume o papel de um herói que deve enfrentar um inimigo em um duelo estratégico de Pedra, Papel e Tesoura, onde cada vitória reduz a vida do oponente.

O projeto foi desenvolvido como tarefa prática para o curso **Python Pro**, demonstrando o uso de interfaces gráficas e lógica de programação funcional.

---

## Funcionalidades
* **Arena Visual**: Interface organizada com o Herói e o Inimigo posicionados lado a lado.
* **Barras de Vida Dinâmicas**: Uso de `ttk.Progressbar` para fornecer feedback visual sobre a vida dos personagens.
* **Lógica de Jokenpô**: Sistema de combate baseado nas regras de Pedra, Papel e Tesoura.
* **Log de Batalha**: Histórico que narra cada round e destaca os resultados com cores dinâmicas no terminal da interface.
* **Tratamento de Assets**: O sistema possui tratamento de erro para carregar as imagens, garantindo a execução mesmo na ausência dos arquivos visuais.

---

## Critérios
Conforme solicitado nas diretrizes da tarefa prática:
1.  **Funções Integradas**: O código utiliza funções nativas das bibliotecas `tkinter`, `random` e `messagebox`.
2.  **requirements.txt**: Arquivo incluso contendo as informações de dependências do projeto.
3.  **Documentação**: Este `README.md` detalha o funcionamento e os objetivos do software.

---

## Para Executar
1.  Certifique-se de ter o Python 3 instalado em sua máquina.
2.  Mantenha os arquivos `hero.png` e `enemy.png` na mesma pasta do script para carregar os visuais.
3.  Execute o comando:
    ```bash
    python3 meu_app.py
    ```

---

## Arquivos
* `meu_app.py`: Código fonte principal.
* `hero.png` / `enemy.png`: Assets visuais da arena.
* `requirements.txt`: Dependências do sistema.
