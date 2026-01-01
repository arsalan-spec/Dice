import tkinter as tk
import random


def roll_dice():

    dice_value = random.randint(1, 6)


    result_label.config(text=f"result: {dice_value}")

    dice_images = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    dice_label.config(text=dice_images[dice_value])



window = tk.Tk()
window.title("Dice roller")
window.geometry("300x400")

title_label = tk.Label(window, text="Dice roller", font=("Arial", 16))
title_label.pack(pady=10)

dice_label = tk.Label(window, text="⚀", font=("Arial", 50))
dice_label.pack(pady=10)

result_label = tk.Label(window, text="result: -", font=("Arial", 14))
result_label.pack(pady=5)

roll_button = tk.Button(window, text="throw a Dice", command=roll_dice, font=("Arial", 12))
roll_button.pack(pady=10)

window.mainloop()