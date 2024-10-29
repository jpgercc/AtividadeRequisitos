import tkinter as tk
import customtkinter as ctk
from PIL import Image
import subprocess
import sys

# Configuração inicial
ctk.set_appearance_mode("system")  # Modos: "dark", "light", "system"
ctk.set_default_color_theme("green")  # Temas: "blue", "green", "dark-blue"

# Criação da janela principal
#LOGO
#logo_image = tk.PhotoImage(file="logo.png")
#self.iconbitmap(logo_image)
root = ctk.CTk()
root.title("Biss Manager - Início")
root.geometry("1200x600")
#root.iconphoto(True, tk.PhotoImage(file="../accets/finalizado.ico"))



# Frame no topo da janela para alinhar os botões
top_frame = ctk.CTkFrame(root)
top_frame.pack(side="top", fill="x", pady=10)

# Função de exemplo para os botões EXCLUIR DEPOIS
def on_button_click(button_number):
    print(f"Botão {button_number} clicado!")

# Função para abrir PAGINAS

def open_funcionarios_page():
    subprocess.Popen([sys.executable, "./src/funcionarios.py"])

def open_clientes_page():
    subprocess.Popen([sys.executable, "./src/clientes.py"])

def open_vendas_page():
    subprocess.Popen([sys.executable, "./src/venda.py"])

def open_historico_page():
    subprocess.Popen([sys.executable, "./src/historico.py"])

def open_produtos_page():
    subprocess.Popen([sys.executable, "./src/produtos.py"])

# Criação dos botões
button1 = ctk.CTkButton(top_frame, text="Realizar Venda", command=open_vendas_page)
button1.pack(side="right", padx=30)

button2 = ctk.CTkButton(top_frame, text="Histórico de Vendas", command=open_historico_page)
button2.pack(side="right", padx=30)

button3 = ctk.CTkButton(top_frame, text="Produtos", command=open_produtos_page)
button3.pack(side="right", padx=30)

button4 = ctk.CTkButton(top_frame, text="Funcionários", command=open_funcionarios_page)
button4.pack(side="left", padx=30)

button5 = ctk.CTkButton(top_frame, text="Clientes", command=open_clientes_page)
button5.pack(side="left", padx=30)

#button1 = ctk.CTkButton(top_frame, text="Sobre a Empresa", command=open_vendas_page)
#button1.pack(side="right", padx=30)

# Carregar a imagem usando PIL
image_path = "./accets/final.png"  # Altere para o caminho da sua imagem
image = Image.open(image_path)
image = image.resize((900, 900), Image.LANCZOS)  # Redimensione a imagem se necessário
# Converter a imagem para CTkImage
ctk_image = ctk.CTkImage(dark_image=image, size=(300, 300))
# Criar um CTkLabel para exibir a imagem
image_label = ctk.CTkLabel(root, image=ctk_image, text="")
image_label.pack(pady=130)  # Posicione a imagem abaixo dos botões

# Loop principal da aplicação
root.mainloop()
