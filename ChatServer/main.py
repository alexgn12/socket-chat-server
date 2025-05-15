from server import ServidorChat

if __name__ == "__main__":
    servidor = ServidorChat("localhost", 46578)
    servidor.iniciar()
