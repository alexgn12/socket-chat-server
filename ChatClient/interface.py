import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from client import ClienteChat

def mostrar_login():
    login = tk.Tk()
    login.title("Login")
    login.geometry("300x150")

    tk.Label(login, text="Nombre de usuario:").pack(pady=10)
    entry_nombre = tk.Entry(login)
    entry_nombre.pack(pady=5)
    entry_nombre.focus()

    def on_login(event=None):
        nombre = entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Introduce un nombre.")
            return

        cliente = ClienteChat("localhost", 46578, nombre)
        if cliente.conectar():
            login.destroy()
            mostrar_chat(cliente)
        else:
            messagebox.showerror("Error", "No se pudo conectar al servidor.")

    boton = tk.Button(login, text="Entrar", command=on_login)
    boton.pack(pady=10)
    entry_nombre.bind("<Return>", on_login)

    login.mainloop()


def mostrar_chat(cliente):
    chat = tk.Tk()
    chat.title("Chat")
    chat.geometry("500x400")

    area_chat = ScrolledText(chat, state='disabled', wrap='word', height=15)
    area_chat.pack(padx=10, pady=10, fill='both', expand=True)

    entrada = tk.Entry(chat)
    entrada.pack(padx=10, pady=(0, 5), fill='x')

    def enviar_mensaje(event=None):
        mensaje = entrada.get()
        if mensaje and cliente.conectado:
            cliente.enviar(mensaje)
            entrada.delete(0, tk.END)

    boton = tk.Button(chat, text="Enviar", command=enviar_mensaje)
    boton.pack(padx=10, pady=(0, 10))
    entrada.bind("<Return>", enviar_mensaje)

    def mostrar_mensaje(mensaje):
        area_chat.config(state='normal')
        area_chat.insert(tk.END, mensaje + "\n")
        area_chat.yview(tk.END)
        area_chat.config(state='disabled')

    cliente.recibir_en_segundo_plano(mostrar_mensaje)
    chat.mainloop()

if __name__ == "__main__":
    mostrar_login()
