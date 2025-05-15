import socket
import threading

class ClienteChat:
    def __init__(self, host, puerto, nombre):
        self.host = host
        self.puerto = puerto
        self.nombre = nombre
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.thread_recepcion = None

    def conectar(self):
        try:
            self.socket.connect((self.host, self.puerto))
            self.socket.send(self.nombre.encode('utf-8'))
            self.conectado = True
            return True
        except Exception as e:
            print(f"[Error] No se pudo conectar: {e}")
            return False
        
    def recibir_en_segundo_plano(self, callback):
        def escuchar():
            while self.conectado:
                try:
                    datos = self.socket.recv(1024)
                    if not datos:
                        break
                    mensaje = datos.decode('utf-8')
                    callback(mensaje)
                except:
                    break
            self.cerrar()

        self.thread_recepcion = threading.Thread(target=escuchar, daemon=True)
        self.thread_recepcion.start()
    
    def enviar(self, mensaje):
        if self.conectado:
            try:
                self.socket.send(mensaje.encode('utf-8'))
            except Exception as e:
                print(f"[Error al enviar] {e}")
                self.cerrar()

    def cerrar(self):
        if self.conectado:
            self.conectado = False
            try:
                self.socket.close()
            except:
                pass
            print("[Cliente] Conexión cerrada.")

