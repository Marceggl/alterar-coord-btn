import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def move_button(button):
    x = random.randint(-200, 200)  # Coordenadas x aleatórias dentro da janela
    y = random.randint(-200, 200)  # Coordenadas y aleatórias dentro da janela
    button.place(x=x, y=y)        # Reposiciona o botão nas novas coordenadas

def mostrar_imagem():
    # Obter o diretório do script atual
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Caminho completo para o arquivo de imagem
    image_path = os.path.join(script_dir, "naoValeEspiar.jpg")
    
    # Carrega a imagem
    image = Image.open(image_path)
    # Abre uma nova janela para exibir a imagem
    image_window = tk.Toplevel()
    image_window.title("Imagem")
    # Converte a imagem para um formato compatível com tkinter
    tk_image = ImageTk.PhotoImage(image)
    # Exibe a imagem em um rótulo na nova janela
    label = ttk.Label(image_window, image=tk_image)
    label.image = tk_image
    label.pack()

    # Centralizar a janela da imagem
    center_window(image_window)

def main():
    gui = tk.Tk()
    gui.geometry("500x500")
    gui.resizable(False, False)
    gui.configure(background="#0D1117")

    texto_btn_nao = "Ele Não é"
    texto_btn_eleE = "Ele é"
    texto_label = "Será que ele é ?"

    labelPergunta = ttk.Label(gui, text=texto_label, font=("Arial", 15))
    labelPergunta.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # Criando um estilo para os botões
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 15))

    btnEleNao = ttk.Button(gui, text=texto_btn_nao, style="TButton")  # Aplicando o estilo ao botão
    btnEleNao.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    btnEleNao.config(command=lambda: move_button(btnEleNao))  # Associando a função move_button ao botão

    btnEleE = ttk.Button(gui, text=texto_btn_eleE, command=mostrar_imagem, style="TButton")  # Aplicando o estilo ao botão
    btnEleE.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    center_window(gui)

    gui.mainloop()


if __name__ == "__main__":
    main()
