import customtkinter as ctk
import random

# Theme setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Raw ASCII hangman stages
HANGMAN_PICS = [
    r"""
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    r"""
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    r"""
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    r"""
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    r"""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========""",
    r"""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========""",
    r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    ========="""
]

# Raw ASCII victory and defeat banners
VICTORY_ART = r"""
 __     __          __          ___        
 \ \   / /          \ \        / (_)     
  \ \_/ /__  _   _   \ \  /\  / / _ _ __ 
   \   / _ \| | | |   \ \/  \/ / | | '_ \
    | | (_) | |_| |    \  /\  /  | | | | | 
    |_|\___/ \__,_|     \/  \/   |_|_| |_|
"""

DEFEAT_ART = r"""
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
"""

# App setup
app = ctk.CTk()
app.title("🎮 Hangman GUI")
app.geometry("700x750")

# Word list
word_list = [
    "python", "hangman", "developer", "interface", "keyboard",
    "graphics", "widget", "program", "function", "variable",
    "loop", "condition", "database", "internet", "machine",
    "learning", "artificial", "intelligence", "neural", "network",
    "algorithm", "debugging", "syntax", "compile", "execute",
    "binary", "framework", "automation", "cloud", "encryption"
]


# Initial state
word = random.choice(word_list).upper()
display_word = ["_" for _ in word]
guessed_letters = set()
tries = 6

# Disable all keyboard buttons
def disable_all_keys():
    for btn in keyboard_buttons:
        btn.configure(state="disabled")

# Update UI
def update_display():
    hangman_label.configure(text=HANGMAN_PICS[6 - tries])
    word_display.configure(text=" ".join(display_word))
    tries_label.configure(text=f"Tries left: {tries}")
    guessed_display.configure(text="Guessed: " + " ".join(sorted(guessed_letters)))

    if "_" not in display_word:
        result_label.configure(text="🎉 You WON!", text_color="green")
        hangman_label.configure(text=VICTORY_ART)
        word_display.configure(text=f"You guessed it! 🎯  {word}", text_color="green")
        disable_all_keys()

    elif tries == 0:
        result_label.configure(text="💀 You LOST!", text_color="red")
        hangman_label.configure(text=DEFEAT_ART)
        word_display.configure(text=f"The word was: {word}", text_color="#ff4d6d")
        disable_all_keys()

# Letter guess logic
def guess_letter(letter):
    global tries
    letter = letter.upper()
    if letter in guessed_letters or tries == 0:
        return
    guessed_letters.add(letter)
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                display_word[i] = letter
    else:
        tries -= 1
    update_display()

# Reset game state
def reset_game():
    global word, display_word, guessed_letters, tries
    word = random.choice(word_list).upper()
    display_word = ["_" for _ in word]
    guessed_letters = set()
    tries = 6
    update_display()
    result_label.configure(text="Guess the word!", text_color="#aaa")
    for btn in keyboard_buttons:
        btn.configure(state="normal")
    word_display.configure(text_color="white")

# Title
ctk.CTkLabel(app, text="HANGMAN", font=("Segoe UI", 32, "bold")).pack(pady=20)

# Hangman ASCII
hangman_label = ctk.CTkLabel(app, text=HANGMAN_PICS[0], font=("Courier", 16), justify="left")
hangman_label.pack()

# Word display
word_display = ctk.CTkLabel(app, text=" ".join(display_word), font=("Segoe UI", 30, "bold"))
word_display.pack(pady=15)

# Tries + guessed
tries_label = ctk.CTkLabel(app, text=f"Tries left: {tries}", font=("Segoe UI", 16))
tries_label.pack()
guessed_display = ctk.CTkLabel(app, text="Guessed: ", font=("Segoe UI", 14))
guessed_display.pack(pady=5)

# Result status
result_label = ctk.CTkLabel(app, text="Guess the word!", font=("Segoe UI", 20, "bold"), text_color="#aaa")
result_label.pack(pady=10)

# Keyboard
keyboard_frame = ctk.CTkFrame(app, fg_color="transparent")
keyboard_frame.pack(pady=20)
keyboard_buttons = []

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i, letter in enumerate(letters):
    btn = ctk.CTkButton(keyboard_frame, text=letter, width=40, command=lambda l=letter: guess_letter(l))
    btn.grid(row=i // 9, column=i % 9, padx=5, pady=5)
    keyboard_buttons.append(btn)

# Reset button
ctk.CTkButton(app, text="🔁 Play Again", fg_color="#ffd369", hover_color="#ffaa00", text_color="black", command=reset_game).pack(pady=30)

# Footer
ctk.CTkLabel(app, text="Made by Mugdha 🖤", font=("Segoe UI", 10), text_color="#666").pack(side="bottom", pady=10)

# Start game
update_display()
app.mainloop()
