import tkinter as tk
from tkinter import ttk, messagebox
import random

hp_max = 100
player_hp = 100
enemy_hp = 100
opcoes = ["Pedra", "Papel", "Tesoura"]
regras = {"Pedra": "Tesoura", "Papel": "Pedra", "Tesoura": "Papel"}

def jogar(escolha_player):
    global player_hp, enemy_hp
    
    escolha_enemy = random.choice(opcoes)
    
    if escolha_player == escolha_enemy:
        resultado = f"EMPATE! Ambos escolheram {escolha_player}."
        cor_log = "yellow"
    elif regras[escolha_player] == escolha_enemy:
        dano = random.randint(15, 25)
        enemy_hp -= dano
        resultado = f"VITÓRIA! {escolha_player} vence {escolha_enemy}. Dano: {dano}"
        cor_log = "#44ff44"
    else:
        dano = random.randint(10, 20)
        player_hp -= dano
        resultado = f"DERROTA! {escolha_enemy} vence {escolha_player}. Dano: {dano}"
        cor_log = "#ff4444"

    barra_player['value'] = player_hp
    barra_enemy['value'] = enemy_hp
    
    log.insert(0, f"Round: {escolha_player} vs {escolha_enemy}")
    log.insert(1, resultado)
    log.itemconfig(1, fg=cor_log)
    
    verificar_fim()

def verificar_fim():
    if enemy_hp <= 0:
        messagebox.showinfo("Fim de Jogo", "O inimigo foi derrotado! Você venceu a masmorra.")
        reset_game()
    elif player_hp <= 0:
        messagebox.showerror("Fim de Jogo", "Você tombou em combate... Tente novamente.")
        reset_game()

def reset_game():
    global player_hp, enemy_hp
    player_hp, enemy_hp = 100, 100
    barra_player['value'] = 100
    barra_enemy['value'] = 100
    log.delete(0, tk.END)

app = tk.Tk()
app.title("Dice & Signs Dungeon")
app.geometry("600x650")
app.configure(bg="#1a1a1a")

try:
    img_hero = tk.PhotoImage(file="hero.png")
    img_enemy = tk.PhotoImage(file="enemy.png")
except:
    img_hero = tk.PhotoImage()
    img_enemy = tk.PhotoImage()

tk.Label(app, text="JOKENPÔ BATTLE", font=("Courier", 24, "bold"), bg="#1a1a1a", fg="gold").pack(pady=10)

frame_arena = tk.Frame(app, bg="#1a1a1a")
frame_arena.pack(pady=20)

frame_p = tk.Frame(frame_arena, bg="#1a1a1a")
frame_p.pack(side=tk.LEFT, padx=30)
canvas_p = tk.Canvas(frame_p, width=150, height=150, bg="#2e2e2e", highlightthickness=2, highlightbackground="blue")
canvas_p.pack()
canvas_p.create_image(75, 75, image=img_hero)
tk.Label(frame_p, text="HERÓI", bg="#1a1a1a", fg="white", font=("Arial", 10, "bold")).pack()
barra_player = ttk.Progressbar(frame_p, length=150, mode='determinate', value=100)
barra_player.pack(pady=5)


frame_e = tk.Frame(frame_arena, bg="#1a1a1a")
frame_e.pack(side=tk.LEFT, padx=30)
canvas_e = tk.Canvas(frame_e, width=150, height=150, bg="#2e2e2e", highlightthickness=2, highlightbackground="red")
canvas_e.pack()
canvas_e.create_image(75, 75, image=img_enemy)
tk.Label(frame_e, text="INIMIGO", bg="#1a1a1a", fg="white", font=("Arial", 10, "bold")).pack()
barra_enemy = ttk.Progressbar(frame_e, length=150, mode='determinate', value=100)
barra_enemy.pack(pady=5)

tk.Label(app, text="ESCOLHA SUA AÇÃO:", bg="#1a1a1a", fg="gray").pack()
frame_botoes = tk.Frame(app, bg="#1a1a1a")
frame_botoes.pack(pady=10)

for op in opcoes:
    btn = tk.Button(frame_botoes, text=op.upper(), width=12, height=2, font=("Arial", 10, "bold"),
                    command=lambda o=op: jogar(o), bg="#333", fg="white", cursor="hand2")
    btn.pack(side=tk.LEFT, padx=10)

log = tk.Listbox(app, width=60, height=10, bg="#000", fg="white", font=("Consolas", 10), borderwidth=0)
log.pack(pady=20, padx=20)

app.mainloop()