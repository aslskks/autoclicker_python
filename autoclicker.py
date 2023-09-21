import tkinter as tk
import pyautogui
import threading

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")

        # Etiqueta
        self.label = tk.Label(root, text="Auto Clicker")
        self.label.pack(pady=10)

        # Botón para activar/desactivar
        self.button = tk.Button(root, text="Activa perro", command=self.toggle_auto_click)
        self.button.pack()

        # Variable para rastrear el estado del auto clicker
        self.auto_clicking = False

    def toggle_auto_click(self):
        if not self.auto_clicking:
            self.auto_clicking = True
            self.button.config(text="Desactivar")
            self.auto_click_thread = threading.Thread(target=self.auto_click)
            self.auto_click_thread.start()
        else:
            self.auto_clicking = False
            self.button.config(text="Activar")

    def auto_click(self):
        while self.auto_clicking:
            posiosion = pyautogui.position()
            pyautogui.click(posiosion)
            # Puedes ajustar la velocidad de clic aquí
            pyautogui.PAUSE = 100

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
