import socket
import threading

class ServidorChat:
    def __init__(self, host, puerto):
        self.host = host
        self.puerto = puerto
        self.servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientes = {}

    def iniciar(self):
        self.servidor_socket.bind((self.host, self.puerto))
        self.servidor_socket.listen(10)
        print(f"Servidor activo en {self.host}:{self.puerto}")

        while True:
            cliente_socket, direccion = self.servidor_socket.accept()
            print(f"Cliente conectado desde {direccion}")
            threading.Thread(target=self._gestionar_cliente, args=(cliente_socket,), daemon=True).start()
    
    def _gestionar_cliente(self, cliente_socket):
        try:
            nombre = cliente_socket.recv(1024).decode('utf-8')
            self.clientes[cliente_socket] = nombre
            print(f"🔔 {nombre} se ha unido al chat")
            self._broadcast(f"🔔 {nombre} se ha unido al chat".encode('utf-8'), cliente_socket)

            while True:
                data = cliente_socket.recv(1024)
                if not data:
                    break

                mensaje = data.decode('utf-8')
                if mensaje.startswith("/"):
                    self._procesar_comando(mensaje, cliente_socket)
                else:
                    self._broadcast(data, cliente_socket)

        except Exception as e:
            print(f"Error con cliente: {e}")
        finally:
            nombre = self.clientes.get(cliente_socket, "Desconocido")
            del self.clientes[cliente_socket]
            self._broadcast(f"❌ {nombre} ha salido del chat".encode('utf-8'), cliente_socket)
            cliente_socket.close()

    def _broadcast(self, mensaje, socket_emisor):
        try:
            mensaje = mensaje.decode('utf-8')
        except:
            mensaje = "<mensaje inválido>"

        nombre_emisor = self.clientes.get(socket_emisor, "Anonimo")
        mensaje_final = f"[{nombre_emisor}]: {mensaje}".encode('utf-8')

        for cliente_socket in self.clientes:
            if cliente_socket != socket_emisor:
                try:
                    cliente_socket.send(mensaje_final)
                except:
                    pass
    
    def _procesar_comando(self, mensaje, cliente_socket):
        if mensaje == "/usuarios":
            lista = ", ".join(self.clientes.values())
            respuesta = f"[Servidor]: Usuarios conectados: {lista}"
            cliente_socket.send(respuesta.encode('utf-8'))
        else:
            cliente_socket.send(f"[Servidor]: Comando no reconocido.".encode('utf-8'))


        


